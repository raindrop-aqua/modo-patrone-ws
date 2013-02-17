# -*- coding: utf-8 -*-

from test.base import GoogleAppEngineTestBase
from application.services.logic.author import AuthorLogic

#class TestAuthorService(GoogleAppEngineTestBase):
#    def test_create(self):
#        service = AuthorLogic()
#        substance = {
#            "name": u"渥美政廣",
#            "mail_address": "mododeveloper@gmail.com",
#            "password": "password"
#        }
#        ret = service.create(substance)
#        ret = str(ret)
#        self.assertGreaterEqual(len(ret), 1)
#
#        substance = {
#            "mail_address": "mododeveloper@gmail.com",
#            "password": "password"
#        }
#        ret = service.create(substance)
#        self.assertEqual(ret, None)
#
#
#    def test_read(self):
#        service = AuthorLogic()
#        substance = {
#            "author_id": "4",
#            "author_mail_address": "mododeveloper@gmail.com",
#        }
#        ret = service.read(substance)
#        self.assertEqual(ret["name"], u"渥美政廣")

#    def test_update(self):
#        service = AuthorService()
#        substance = {
#            "name": u"渥美政廣",
#            "mail_address": "mododeveloper@gmail.com",
#            "password": "abcde"
#        }
#        ret = service.create(substance)
#        ret = str(ret)
#        self.assertGreaterEqual(len(ret), 1)

#    def test_list(self):
#        service = AuthorService()
#        ret = service.list()
#        self.assertGreaterEqual(len(ret.items()), 1)

#    def test__validate(self):
#        service = AuthorService()
#        substance = {
#            "name": u"渥美政廣",
#            "mail_address": "mododeveloper@gmail.com",
#            "password": "password"
#        }
#        self.assertEqual(service._validate(substance), True)
#        self.assertEqual(service._validate(None), False)
#        self.assertEqual(service._validate({}), False)

#    def test_aaa(self):
#        service = AuthorService()
#        self.assertEqual(service.aaa(), "aaa")
