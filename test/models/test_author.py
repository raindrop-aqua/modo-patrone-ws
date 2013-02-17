# -*- coding: utf-8 -*-
from unittest import TestCase
from application.models.author import Author
from test.base import GoogleAppEngineTestBase


class TestAuthor(GoogleAppEngineTestBase):
    def test_to_hash(self):
        author = Author(
            mail_address="aaa@bbb.com",
            author_name="test user",
            password="test password",
        )
        author_key = author.put()
        author.to_hash()
        self.assertEqual(1, 1)



















    def test_exists_by_mail_address(self):
        self.fail()

    def test__get_author_id_by_mail_address(self):
        self.fail()

    def test_make_author_id_hash(self):
        self.fail()

    def test_make_password_hash(self):
        self.fail()

    def test_login(self):
        self.fail()

    def test_is_login(self):
        self.fail()

    def test__login(self):
        self.fail()

    def test__make_token(self):
        self.fail()