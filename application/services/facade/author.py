# -*- coding: utf-8 -*-

import logging

from application.services.logic.author import AuthorLogic
from application.services.proxy.author import AuthorProtectionProxy
from application.utils import const
from application.utils.exceptions import IllegalRequestError
from application.utils.exceptions import IllegalAccessError
from application.utils.exceptions import AlreadyRegisteredError
from application.utils.exceptions import NoDataError


class AuthorFacade(object):
    @classmethod
    def create(cls, request):

        result = const.RESPONSE_RESULT_FAILED

        try:
            if not AuthorFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            AuthorLogic.create(substance)
        except IllegalRequestError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except IllegalAccessError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except AlreadyRegisteredError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except Exception, ex:
            logging.error(ex.message)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, None)

    @classmethod
    def read(cls, request):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not AuthorFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            res = AuthorLogic.read(substance)
        except IllegalRequestError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except NoDataError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except Exception, ex:
            logging.error(ex.message)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, res)

    @classmethod
    def update(cls, request, secure=True):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not AuthorFacade._validate(request):
                raise IllegalRequestError(None)
            if secure:
                res = AuthorProtectionProxy.update(request)
            else:
                substance = request.get("substance")
                res = AuthorLogic.update(substance)
        except AlreadyRegisteredError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except IllegalRequestError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except IllegalAccessError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except Exception, ex:
            logging.error(ex)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, res)


    @classmethod
    def update_password(cls, request, secure=True):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not AuthorFacade._validate(request):
                raise IllegalRequestError(None)
            if secure:
                res = AuthorProtectionProxy.update_password(request)
            else:
                substance = request.get("substance")
                res = AuthorLogic.update_password(substance)
        except IllegalRequestError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except IllegalAccessError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except Exception, ex:
            logging.error(ex)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, res)


    @classmethod
    def authentication(cls, request):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not AuthorFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            res = AuthorLogic.authentication(substance)
        except IllegalRequestError, ex:
            message = ex.message
            logging.warn(ex.message + str(request))
        except Exception, ex:
            logging.error(ex)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, res)


    @classmethod
    def list(cls):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            res = AuthorLogic.list()
        except Exception, ex:
            logging.error(ex.message)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return AuthorFacade._make_response(result, message, res)


    @classmethod
    def _validate(cls, request):
        if not request:
            return False
        return True


    @classmethod
    def _make_response(cls, result, message, substance):
        ret = dict({
            "response": {
                "result": result,
                "message": message
            }
        })
        if substance:
            ret["response"]["substance"] = substance

        return ret
