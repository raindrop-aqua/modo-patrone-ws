# -*- coding: utf-8 -*-

from flask import Module, jsonify, request, abort, send_file

from application.services.facade.kit import KitFacade
from application.utils import const

kit_api = Module(__name__)


@kit_api.route("/kit/create", methods=["GET", "POST"])
def create_kit():
    json = {
        "request": {
            "credential": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "token": "b941295b36824f0fc19cc473ba9d6b67866b2709"
            },
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "kit_name": u"My Wonderful Kit",
                "category_id": "253b16bf5d78bd4bb3af19ed874c4468e759f2d0",
                "tags": ["render", "camera"],
                "description": u"これはmodoの素晴らしいキットです。\nみなさんぜひご利用ください。",
            }
        }

    }
    req = json.get("request")
    res = KitFacade.create(req)
    return jsonify(res)


@kit_api.route("/kit/read/<kit_id>", methods=["GET"])
def read_kit(kit_id):
    json = {
        "request": {
            "substance": {
                "kit_id": kit_id,
            }
        }
    }
    req = json.get("request")
    res = KitFacade.read(req)
    return jsonify(res)


@kit_api.route("/kit/update", methods=["GET", "POST"])
def update_kit():
    json = {
        "request": {
            "credential": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "token": "b941295b36824f0fc19cc473ba9d6b67866b2709"
            },
            "substance": {
                "kit_id": "3b1efa98eac78dd9a887b949c07bc739fcd2d044",
                "kit_name": u"My Wonderful Kit Review!",
                "category_id": "c1ac4c51afdd9ed6df0d3d871d38f261b70dcba8",
                "tags": [u"geo"],
                "description": u"これはmodoの素晴らしいキットです。\nみなさんぜひご利用ください。\n内容を改変しました。",
                "valid": True,
            }
        }
    }

    req = json.get("request")
    res = KitFacade.update(req)
    return jsonify(res)


@kit_api.route("/kit/download/<kit_id>", methods=["GET"])
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


@kit_api.route("/kit/list", methods=["POST"])
def list_kit():
    res = KitFacade.list(request.json)
    return jsonify(res)
