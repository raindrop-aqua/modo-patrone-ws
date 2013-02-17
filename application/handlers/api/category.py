# -*- coding: utf-8 -*-

from flask import Module, jsonify
from application.services.facade.category import CategoryFacade

category_api = Module(__name__)


@category_api.route("/category/list")
def list_category():
    res = CategoryFacade.list()
    return jsonify(res)

# @category_api.route("/category/init")
# def init_category():
#     res = CategoryFacade.init()
#     return jsonify(res)
