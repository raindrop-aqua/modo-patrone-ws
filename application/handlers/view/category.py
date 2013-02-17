# -*- coding: utf-8 -*-

from flask import Module, redirect
from flask.templating import render_template

from application.services.facade.category import CategoryFacade

category_view = Module(__name__)


@category_view.route("/admin/category/list", methods=["GET"])
def list_category():
    res = CategoryFacade.list()
    categories = res.get("response").get("substance").get("items")
    return render_template("category/list.html", categories=categories)


@category_view.route("/admin/category/init")
def init_category():
    CategoryFacade.init()
    return redirect("/admin/category/list")
