# -*- coding: utf-8 -*-

from application.models.author import Author
from application.services.logic.kit import KitLogic
from application.utils.exceptions import IllegalRequestError, IllegalAccessError


class KitProtectionProxy(object):
    @classmethod
    def create(cls, request):
        credential = request.get("credential")
        KitProtectionProxy._authenticated(credential)

        substance = request.get("substance")
        KitLogic.create(substance)

    @classmethod
    def update(cls, request):
        credential = request.get("credential")
        KitProtectionProxy._authenticated(credential)

        substance = request.get("substance")
        KitLogic.update(substance)

    @classmethod
    def _authenticated(cls, credential):
        author_id = credential.get("author_id")
        token = credential.get("token")

        if not KitProtectionProxy._validate(credential):
            raise IllegalRequestError(None)
        if not Author.is_login(author_id, token):
            raise IllegalAccessError(None)

    @classmethod
    def _validate(cls, credential):
        if not credential:
            return False
        if not credential.get("author_id"):
            return False
        if not credential.get("token"):
            return False
        return True

    def _diff_id(self, credential, substance):
        if not credential:
            return False
        if not substance:
            return False
        if credential.get("author_id") != substance.get("author_id"):
            return False
        return True
