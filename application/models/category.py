# -*- coding: utf-8 -*-

from datetime import datetime
import hashlib

from google.appengine.ext import ndb
from application.utils import const


class Category(ndb.Model):
    category_name = ndb.StringProperty()
    valid = ndb.BooleanProperty(default=True)
    create_datetime = ndb.DateTimeProperty(auto_now_add=True)
    update_datetime = ndb.DateTimeProperty(auto_now=True)

    def to_hash(self):
        return {
            "category_id": self.key.string_id(),
            "category_name": self.category_name,
            "valid": self.valid,
            "create_datetime": self.create_datetime.strftime(const.DATETIME_FORMAT),
            "update_datetime": self.update_datetime.strftime(const.DATETIME_FORMAT),
        }

    @classmethod
    def get_key_by_id(cls, category_id):
        if not category_id:
            return None
        category = Category.get_by_id(category_id)
        if not category:
            return None
        return category.key

    @classmethod
    def make_category_id_hash(cls):
        src = "Category" + str(datetime.now())
        return hashlib.sha1(src).hexdigest()
