# -*- coding: utf-8 -*-

from datetime import datetime
import hashlib

from google.appengine.ext import ndb
from application.utils import const


class Kit(ndb.Model):
    kit_name = ndb.StringProperty(required=True)
    author = ndb.KeyProperty(kind="Author")
    download_count = ndb.IntegerProperty(default=0, indexed=False)
    view_count = ndb.IntegerProperty(default=0, indexed=False)
    category = ndb.KeyProperty(kind="Category")
    tags = ndb.StringProperty(repeated=True)
    description = ndb.TextProperty(indexed=False)
    valid = ndb.BooleanProperty(default=False)
    kit_file_id = ndb.BlobKeyProperty()
    create_datetime = ndb.DateTimeProperty(auto_now_add=True)
    update_datetime = ndb.DateTimeProperty(auto_now=True)

    def inc_download_count(self):
        self.download_count += 1
        self.put()

    def inc_view_count(self):
        self.view_count += 1
        self.put()

    def to_hash_short(self):
        category_name = None
        if self.category:
            category_name = self.category.get().category_name

        return {
            "kit_id": self.key.string_id(),
            "kit_name": self.kit_name,
            "download_count": self.download_count,
            "category_name": category_name,
            "view_count": self.view_count,
            "valid": self.valid,
            "create_datetime": self.create_datetime.strftime(const.DATETIME_FORMAT),
            "update_datetime": self.update_datetime.strftime(const.DATETIME_FORMAT),
        }

    def to_hash(self):
        author = None
        if self.author:
            author = self.author.get().to_hash()
        category = None
        if self.category:
            category = self.category.get().to_hash()

        return {
            "kit_id": self.key.string_id(),
            "kit_name": self.kit_name,
            "author": author,
            "download_count": self.download_count,
            "view_count": self.view_count,
            "category": category,
            "tags": self.tags,
            "description": self.description,
            "valid": self.valid,
            "kit_file_id": self.kit_file_id,
            "create_datetime": self.create_datetime.strftime(const.DATETIME_FORMAT),
            "update_datetime": self.update_datetime.strftime(const.DATETIME_FORMAT),
        }

    @classmethod
    def sanitize_tags(cls, tags):
        if not tags:
            return []
        return [unicode(tag).strip() for tag in tags]

    @classmethod
    def make_kit_id_hash(cls):
        src = "Kit" + str(datetime.now())
        return hashlib.sha1(src).hexdigest()
