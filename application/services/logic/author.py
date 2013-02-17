# -*- coding: utf-8 -*-


from application.models.author import Author
from application.utils.exceptions import IllegalRequestError
from application.utils.exceptions import AlreadyRegisteredError
from application.utils.exceptions import NoDataError


class AuthorLogic(object):
    @classmethod
    def create(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            if not substance.get("author_name"):
                return False
            if not substance.get("mail_address"):
                return False
            if not substance.get("password"):
                return False
            return True

        if not _validate(substance):
            raise IllegalRequestError(None)
        if Author.exists_by_mail_address(substance.get("mail_address")):
            raise AlreadyRegisteredError(None)

        author = Author(
            id=Author.make_author_id_hash(),
            author_name=substance.get("author_name"),
            password=Author.make_password_hash(substance.get("password")),
            mail_address=substance.get("mail_address")
        )
        author.put()
        return True

    @classmethod
    def read(cls, substance):
        author_id = substance.get("author_id")

        if not author_id:
            raise IllegalRequestError(None)

        author = Author.get_by_id(author_id)
        if not author:
            raise NoDataError(None)
        return author.to_hash()

    @classmethod
    def update(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            if not substance.get("author_name"):
                return False
            if not substance.get("mail_address"):
                return False
            return True

        author_id = substance.get("author_id")
        author_name = substance.get("author_name")
        mail_address = substance.get("mail_address")
        valid = substance.get("valid")

        if not _validate(substance):
            raise IllegalRequestError(None)

        author = Author.get_by_id(author_id)
        if not author:
            raise NoDataError(None)
        if author.mail_address != mail_address:
            if Author.exists_by_mail_address(substance.get("mail_address")):
                raise AlreadyRegisteredError(None)

        author.author_name = author_name
        author.mail_address = mail_address
        author.valid = valid
        author.put()

    @classmethod
    def update_password(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            if not substance.get("author_id"):
                return False
            if not substance.get("password"):
                return False
            return True

        author_id = substance.get("author_id")
        password = substance.get("password")

        if not _validate(substance):
            raise IllegalRequestError(None)

        author = Author.get_by_id(author_id)
        if not author:
            raise NoDataError(None)
        author.password = Author.make_password_hash(password)
        author.put()

    @classmethod
    def release_provisional(cls, substance):
        author_id = substance.get("author_id")

        if not author_id:
            raise IllegalRequestError(None)

        author = Author.get_by_id(author_id)
        if not author:
            raise NoDataError(None)
        author.provisional = False
        author.put()

    @classmethod
    def list(cls):
        author_list = [author.to_hash() for author in Author.query()]
        return dict(items=author_list)

    @classmethod
    def authentication(cls, substance):
        def _validate(substance):
            if not substance:
                return False
            if not substance.get("author_id"):
                return False
            if not substance.get("password"):
                return False
            return True

        mail_address = substance.get("mail_address")
        password = substance.get("password")

        if not _validate(substance):
            raise IllegalRequestError(None)

        token = Author.login(mail_address, password)
        if token:
            result = True
        else:
            result = False
        return dict(token=token, result=result)
