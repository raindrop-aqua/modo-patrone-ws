# -*- coding: utf-8 -*-

import logging

from google.appengine.api import files
from google.appengine.ext.ndb import blobstore

from application.models.author import Author
from application.models.category import Category
from application.models.kit import Kit
from application.utils.exceptions import IllegalRequestError
from application.utils.exceptions import NoDataError
from werkzeug.utils import secure_filename


class KitLogic(object):
    @classmethod
    def create(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            return True

        if not _validate(substance):
            raise IllegalRequestError(None)

        author_id = substance.get("author_id")
        author_key = Author.get_key_by_id(author_id)

        category_id = substance.get("category_id")
        category_key = Category.get_key_by_id(category_id)

        kit = Kit(
            id=Kit.make_kit_id_hash(),
            kit_name=substance.get("kit_name"),
            author=author_key,
            category=category_key,
            tags=Kit.sanitize_tags(substance.get("tags")),
            description=substance.get("description"),
        )
        if substance.get("kit_file"):
            kit.kit_file_id = KitLogic._store_to_blobstore(substance.get("kit_file"))
        kit.put()
        return True

    @classmethod
    def read(cls, substance):
        kit_id = substance.get("kit_id")

        if not kit_id:
            raise IllegalRequestError(None)

        kit = Kit.get_by_id(kit_id)
        if not kit:
            raise NoDataError(None)
        kit.inc_view_count()
        return kit.to_hash()

    @classmethod
    def update(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            if not substance.get("kit_name"):
                return False
            return True

        kit_id = substance.get("kit_id")

        if not _validate(substance):
            raise IllegalRequestError(None)

        kit = Kit.get_by_id(kit_id)
        if not kit:
            raise NoDataError(None)

        kit_name = substance.get("kit_name")
        category_id = substance.get("category_id")
        category_key = Category.get_key_by_id(category_id)

        kit.kit_name = kit_name
        kit.description = substance.get("description")
        kit.category = category_key
        kit.tags = Kit.sanitize_tags(substance.get("tags"))
        kit.valid = substance.get("valid")
        if substance.get("kit_file"):
            if kit.kit_file_id:
                KitLogic._delete_from_blobstore(str(kit.kit_file_id))
            kit.kit_file_id = KitLogic._store_to_blobstore(substance.get("kit_file"))
        kit.put()

    @classmethod
    def download(cls, substance):
        kit_id = substance.get("kit_id")

        if not kit_id:
            raise IllegalRequestError(None)

        kit = Kit.get_by_id(kit_id)
        if not kit or not kit.kit_file_id:
            raise NoDataError(None)
        kit_file = blobstore.BlobReader(str(kit.kit_file_id))
        kit.inc_download_count()
        return dict(kit_file=kit_file)

    @classmethod
    def list(cls, substance):
        kit_list = []
        author_id = substance.get("author_id")
        category_id = substance.get("category_id")
        tags = substance.get("tags")
        if author_id:
            author_key = Author.get_key_by_id(author_id)
            if author_key:
                kit_list = [kit.to_hash_short() for kit in Kit.query(Kit.author == author_key)]
        elif category_id:
            category_key = Category.get_key_by_id(category_id)
            if category_key:
                kit_list = [kit.to_hash_short() for kit in Kit.query(Kit.category == category_key, True == Kit.valid)]
        elif tags:
            kit_list = [kit.to_hash_short() for kit in
                        Kit.query(Kit.tags.IN(Kit.sanitize_tags(tags)), True == Kit.valid)]
        else:
            kit_list = [kit.to_hash_short() for kit in Kit.query(True == Kit.valid)]
        return dict(items=kit_list)

    @classmethod
    def _store_to_blobstore(cls, file_data):
        blob_io = files.blobstore.create(mime_type=file_data.content_type,
                                         _blobinfo_uploaded_filename=secure_filename(file_data.filename))
        with files.open(blob_io, "a") as f:
            for chunk in file_data.stream:
                f.write(chunk)
        files.finalize(blob_io)
        return files.blobstore.get_blob_key(blob_io)

    @classmethod
    def _delete_from_blobstore(cls, file_id):
        logging.info("Blob Deleting: %s" % file_id)
        blobstore.delete(file_id)
        if not blobstore.get(file_id):
            logging.info("Blob Deleted : %s" % file_id)
