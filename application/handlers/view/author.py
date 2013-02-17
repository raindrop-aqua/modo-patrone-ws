# -*- coding: utf-8 -*-

from flask import Module, render_template, request, redirect

from application.forms.author import CreateForm, UpdateForm, UpdatePasswordForm
from application.services.facade.author import AuthorFacade
from application.services.facade.kit import KitFacade
from application.utils import const

author_view = Module(__name__)


@author_view.route("/admin/author/list")
def list_author():
    res = AuthorFacade.list()
    authors = res.get("response").get("substance").get("items")
    return render_template("author/list.html", authors=authors)


@author_view.route("/admin/author/create", methods=["GET"])
def get_create_author():
    form = CreateForm(csrf_enabled=False)
    return render_template("author/create.html", form=form)


@author_view.route("/admin/author/create", methods=["POST"])
def post_create_author():
    form = CreateForm(request.form, csrf_enabled=False)
    if form.validate():
        json = {
            "request": {
                "substance": {
                    "author_name": form.author_name.data,
                    "mail_address": form.mail_address.data,
                    "password": form.password.data,
                }
            }
        }
        req = json.get("request")
        ret = AuthorFacade.create(req).get("response")
        if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
            return redirect("/admin/author/list")
        else:
            form.errors["exceptions"] = [ret.get("message")]
    return render_template("author/create.html", form=form)


@author_view.route("/admin/author/update/<author_id>", methods=["GET"])
def update_author(author_id):
    form = UpdateForm(csrf_enabled=False)
    json = {
        "request": {
            "substance": {
                "author_id": author_id,
            }
        }
    }
    req = json.get("request")
    ret = AuthorFacade.read(req).get("response")
    if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
        substance = ret.get("substance")

        form.author_id.data = substance.get("author_id")
        form.author_name.data = substance.get("author_name")
        form.mail_address.data = substance.get("mail_address")
        form.valid.data = str(substance.get("valid"))
    else:
        return redirect("/admin/author/create")

    json = {
        "request": {
            "substance": {
                "author_id": author_id
            }
        }
    }
    req = json.get("request")
    res = KitFacade.list(req)
    kits = res.get("response").get("substance").get("items")
    return render_template("author/update.html", form=form, kits=kits)


@author_view.route("/admin/author/update/<author_id>", methods=["POST"])
def post_update_author(author_id):
    form = UpdateForm(request.form, csrf_enabled=False)
    if form.validate():
        json = {
            "request": {
                "substance": {
                    "author_id": form.author_id.data,
                    "author_name": form.author_name.data,
                    "mail_address": form.mail_address.data,
                    "valid": True if form.valid.data == "True" else False,
                }
            }
        }
        req = json.get("request")
        ret = AuthorFacade.update(req, secure=False).get("response")
        if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
            return redirect("/admin/author/list")
        else:
            form.errors["exceptions"] = [ret.get("message")]

    json = {
        "request": {
            "substance": {
                "author_id": author_id
            }
        }
    }
    req = json.get("request")
    res = KitFacade.list(req)
    kits = res.get("response").get("substance").get("items")
    return render_template("author/update.html", form=form, kits=kits)


@author_view.route("/admin/author/update_password/<author_id>", methods=["GET"])
def get_update_password_author(author_id):
    json = {
        "request": {
            "substance": {
                "author_id": author_id,
            }
        }
    }
    req = json.get("request")
    ret = AuthorFacade.read(req).get("response")
    if not ret or ret.get("result") != const.RESPONSE_RESULT_SUCCESSFUL:
        return redirect("/admin/author/create")

    form = UpdatePasswordForm(csrf_enabled=False)
    form.author_id.data = author_id

    json = {
        "request": {
            "substance": {
                "author_id": author_id
            }
        }
    }
    req = json.get("request")
    res = KitFacade.list(req)
    kits = res.get("response").get("substance").get("items")
    return render_template("author/update_password.html", form=form, kits=kits)


@author_view.route("/admin/author/update_password/<author_id>", methods=["POST"])
def post_update_password_author(author_id):
    form = UpdatePasswordForm(request.form, csrf_enabled=False)
    if form.validate():
        json = {
            "request": {
                "substance": {
                    "author_id": form.author_id.data,
                    "password": form.password.data,
                }
            }
        }
        req = json.get("request")
        ret = AuthorFacade.update_password(req, secure=False).get("response")
        if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
            return redirect("/admin/author/list")
        else:
            form.errors["exceptions"] = [ret.get("message")]

    json = {
        "request": {
            "substance": {
                "author_id": author_id
            }
        }
    }
    req = json.get("request")
    res = KitFacade.list(req)
    kits = res.get("response").get("substance").get("items")
    return render_template("author/update_password.html", form=form, kits=kits)
