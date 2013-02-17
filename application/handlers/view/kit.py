# -*- coding: utf-8 -*-

from flask import Module, render_template, request, redirect, send_file, abort

from application.forms.kit import CreateForm, UpdateForm
from application.services.facade.kit import KitFacade
from application.utils import const


kit_view = Module(__name__)


@kit_view.route("/admin/kit/list")
def list_kit():
    json = {
        "request": {
            "substance": {
            }
        }
    }
    req = json.get("request")
    res = KitFacade.list(req)
    kits = res.get("response").get("substance").get("items")
    return render_template("kit/list.html", kits=kits)


@kit_view.route("/admin/kit/create", methods=["GET"])
def get_create_kit():
    author_id = request.values["author_id"]
    form = CreateForm(csrf_enabled=False)
    form.init()
    form.author_id.data = author_id
    return render_template("kit/create.html", form=form)


@kit_view.route("/admin/kit/create", methods=["POST"])
def post_create_kit():
    form = CreateForm(csrf_enabled=False)
    form.init()
    form.process(request.form)
    kit_file = request.files["kit_file"]

    if form.validate():
        json = {
            "request": {
                "substance": {
                    "kit_name": form.kit_name.data,
                    "author_id": form.author_id.data,
                    "category_id": form.category_id.data,
                    "tags": unicode(form.tags.data).split(","),
                    "description": form.description.data,
                    "kit_file": kit_file,
                }
            }
        }
        req = json.get("request")
        ret = KitFacade.create(req).get("response")
        if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
            return redirect("/admin/author/update/" + form.author_id.data)
        else:
            form.errors["exceptions"] = [ret.get("message")]
    return render_template("kit/create.html", form=form)


@kit_view.route("/admin/kit/update/<kit_id>", methods=["GET"])
def get_update_kit(kit_id):
    form = UpdateForm(csrf_enabled=False)
    form.init()
    json = {
        "request": {
            "substance": {
                "kit_id": kit_id,
            }
        }
    }
    req = json.get("request")
    ret = KitFacade.read(req).get("response")
    if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
        substance = ret.get("substance")

        form.kit_id.data = substance.get("kit_id")
        form.kit_name.data = substance.get("kit_name")
        form.author_id.data = substance.get("author").get("author_id")
        form.category_id.data = substance.get("category").get("category_id")
        form.tags.data = ",".join(substance.get("tags"))
        form.description.data = substance.get("description")
        form.valid.data = str(substance.get("valid"))
    else:
        return redirect("/admin/author/list")
    return render_template("kit/update.html", form=form)


@kit_view.route("/admin/kit/update/<kit_id>", methods=["POST"])
def post_update_kit(kit_id):
    form = UpdateForm(csrf_enabled=False)
    form.init()
    form.process(request.form)
    kit_file = request.files["kit_file"]

    if form.validate():
        json = {
            "request": {
                "substance": {
                    "kit_id": form.kit_id.data,
                    "kit_name": form.kit_name.data,
                    "category_id": form.category_id.data,
                    "tags": unicode(form.tags.data).split(","),
                    "description": form.description.data,
                    "kit_file": kit_file,
                    "valid": True if form.valid.data == "True" else False,
                }
            }
        }
        req = json.get("request")
        ret = KitFacade.update(req, secure=False).get("response")
        if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
            return redirect("/admin/author/update/" + form.author_id.data)
        else:
            form.errors["exceptions"] = [ret.get("message")]
    return render_template("kit/update.html", form=form)


@kit_view.route("/admin/kit/download/<kit_id>", methods=["GET"])
def download_kit(kit_id):
    json = {
        "request": {
            "substance": {
                "kit_id": kit_id,
            }
        }
    }
    req = json.get("request")
    ret = KitFacade.download(req).get("response")
    if ret and ret.get("result") == const.RESPONSE_RESULT_SUCCESSFUL:
        substance = ret.get("substance")
        kit_file = substance.get("kit_file")
        return send_file(filename_or_fp=kit_file, attachment_filename=kit_file.blob_info.filename, as_attachment=True)
    else:
        abort(404)