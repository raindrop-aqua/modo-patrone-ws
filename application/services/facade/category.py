# -*- coding: utf-8 -*-

import logging

from application.services.logic.category import CategoryLogic
from application.utils import const


class CategoryFacade(object):
    @classmethod
    def init(cls):
        result = const.RESPONSE_RESULT_FAILED

        try:
            CategoryLogic.init()
        except Exception, ex:
            logging.error(ex.message)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return CategoryFacade._make_response(result, message, None)

    @classmethod
    def list(cls):
        result = const.RESPONSE_RESULT_FAILED
        res = None

        try:
            res = CategoryLogic.list()
        except Exception, ex:
            logging.error(ex.message)
            message = const.MESSAGE_FAILED
        else:
            result = const.RESPONSE_RESULT_SUCCESSFUL
            message = const.MESSAGE_SUCCESSFUL

        return CategoryFacade._make_response(result, message, res)

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
