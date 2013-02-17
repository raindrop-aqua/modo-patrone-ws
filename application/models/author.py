# -*- coding: utf-8 -*-

import logging

from datetime import datetime
import hashlib

from google.appengine.ext import ndb
from google.appengine.api import memcache

from application.utils import const
from application.utils.exceptions import IllegalRequestError


class Author(ndb.Model):
    author_name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    mail_address = ndb.StringProperty(required=True)
    provisional = ndb.BooleanProperty(default=True)
    valid = ndb.BooleanProperty(default=True)
    create_datetime = ndb.DateTimeProperty(auto_now_add=True)
    update_datetime = ndb.DateTimeProperty(auto_now=True)

    def to_hash(self):
        return {
            "author_id": self.key.string_id(),
            "author_name": self.author_name,
            "mail_address": self.mail_address,
            "provisional": self.provisional,
            "valid": self.valid,
            "create_datetime": self.create_datetime.strftime(const.DATETIME_FORMAT),
            "update_datetime": self.update_datetime.strftime(const.DATETIME_FORMAT),
        }

    @classmethod
    def exists_by_mail_address(cls, mail_address):
        query = Author.query(Author.mail_address == mail_address)
        if query.count() > 0:
            return True
        else:
            return False

    @classmethod
    def _get_author_id_by_mail_address(cls, mail_address):
        query = Author.query(Author.mail_address == mail_address)
        for author in query:
            return author.key.string_id()

    @classmethod
    def get_key_by_id(cls, author_id):
        if not author_id:
            return None
        author = Author.get_by_id(author_id)
        if not author:
            return None
        return author.key

    @classmethod
    def make_author_id_hash(cls):
        src = "Author" + str(datetime.now())
        return hashlib.sha1(src).hexdigest()

    @classmethod
    def make_password_hash(cls, password):
        if not password:
            raise IllegalRequestError(None)
        return hashlib.sha1(password).hexdigest()

    @classmethod
    def _make_token(cls, author_id):
        if not author_id:
            return None
        source = author_id + datetime.today().strftime(const.DATETIME_FORMAT)
        return hashlib.sha1(source).hexdigest()

    @classmethod
    def login(cls, mail_address, password):
        logging.info("Trying login %s : %s" % (mail_address, password))
        if not mail_address or not password:
            return None
        author_id = Author._get_author_id_by_mail_address(mail_address)
        if not author_id:
            return None

        author = Author.get_by_id(author_id)
        if author and author.password == Author.make_password_hash(password):
            token = Author._make_token(author_id)
            if not Author._login(author_id, token):
                return None
            return token
        else:
            logging.info("Login failed %s : %s" % (mail_address, password))
            return None

    @classmethod
    def is_login(cls, author_id, token):
        if not token:
            return False
        if memcache.get(namespace=const.NAMESPACE_LOGIN, key=author_id) == token:
            return Author._login(author_id, token)
        else:
            return False

    @classmethod
    def _login(cls, author_id, token):
        return memcache.set(
            namespace=const.NAMESPACE_LOGIN,
            key=author_id,
            value=token,
            time=const.LOGIN_TIMEOUT
        )
