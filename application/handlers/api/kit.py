# -*- coding: utf-8 -*-

from flask import Module, jsonify
from application.services.facade.kit import KitFacade

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


@kit_api.route("/kit/read")
def read_kit():
    json = {
        "request": {
            "substance": {
                "kit_id": "3b1efa98eac78dd9a887b949c07bc739fcd2d044",
            }
        }
    }

    req = json.get("request")
    res = KitFacade.read(req)
    return jsonify(res)


@kit_api.route("/kit/update", methods=["GET", "POSt"])
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


@kit_api.route("/kit/download")
def download_kit():
    json = {
        "request": {
            "substance": {
                "kit_id": "3b1efa98eac78dd9a887b949c07bc739fcd2d044",
            }
        }
    }

    req = json.get("request")
    res = KitFacade.download(req)
    return jsonify(res)


@kit_api.route("/kit/list")
def list_kit():
    json = {
        "request": {
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
#                "category_id": "c1ac4c51afdd9ed6df0d3d871d38f261b70dcba8",
#                "tags": []
            }
        }
    }

    req = json.get("request")
    res = KitFacade.list(req)
    return jsonify(res)
