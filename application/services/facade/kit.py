# -*- coding: utf-8 -*-

import logging

from application.services.logic.kit import KitLogic
from application.services.proxy.kit import KitProtectionProxy
from application.utils.exceptions import IllegalRequestError
from application.utils.exceptions import IllegalAccessError
from application.utils.exceptions import AlreadyRegisteredError
from application.utils.exceptions import NoDataError
from application.utils import const


class KitFacade(object):
    @classmethod
    def create(cls, request):

        result = const.RESPONSE_RESULT_FAILED

        try:
            if not KitFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            KitLogic.create(substance)
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

        return KitFacade._make_response(result, message, None)

    @classmethod
    def read(cls, request):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not KitFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            res = KitLogic.read(substance)
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

        return KitFacade._make_response(result, message, res)

    @classmethod
    def update(cls, request, secure=True):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not KitFacade._validate(request):
                raise IllegalRequestError(None)
            if secure:
                res = KitProtectionProxy.update(request)
            else:
                substance = request.get("substance")
                res = KitLogic.update(substance)
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

        return KitFacade._make_response(result, message, res)

    @classmethod
    def list(cls, request):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not KitFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            res = KitLogic.list(substance)
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

        return KitFacade._make_response(result, message, res)

    @classmethod
    def download(cls, request):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            if not KitFacade._validate(request):
                raise IllegalRequestError(None)

            substance = request.get("substance")
            res = KitLogic.download(substance)
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

        return KitFacade._make_response(result, message, res)

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

