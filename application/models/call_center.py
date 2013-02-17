# -*- coding: utf-8 -*-

import datetime
import hashlib
from google.appengine.ext import ndb
from author import Author

class CallCenter(ndb.Model):
    author = ndb.KeyProperty(Author)
    # mail_address and create_datetime with SHA1
    onetime_code = ndb.StringProperty()
    # author_release_provisional | forget_password
    function = ndb.StringProperty()
    valid = ndb.BooleanProperty(default=True)
    create_datetime = ndb.DateTimeProperty(auto_now_add=True)
    update_datetime = ndb.DateTimeProperty(auto_now=True)

    def __init__(self, author=author, **kwds):
        super(CallCenter, self).__init__(**kwds)
        self.author = author

    def _make_onetime_code(self):
        now = datetime.datetime.now()
        un_hash_code = self.author.mail_address + now.strftime("%Y-%m-%d %H:%M:%S")
        return hashlib.sha1(un_hash_code).hexdigest()
