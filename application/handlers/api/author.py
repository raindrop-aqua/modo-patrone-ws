# -*- coding: utf-8 -*-
from flask import Module, jsonify, request
from application.services.facade.author import AuthorFacade

author_api = Module(__name__)


@author_api.route("/author/create", methods=["GET", "POST"])
def create_author():
    json = {
        "request": {
            "substance": {
                "author_name": u"Masahiro Atsumi",
                "mail_address": "raindrop.aqua@gmail.com",
                "password": "password"
            }
        }
    }
    #    json = {
    #        "request": {
    #            "credential": {
    #                "author_id": "mododeveloper@gmail.com",
    #                "token": "1234567890abcde",
    #                },
    #            "substance": {
    #                "author_name": u"渥美政廣",
    #                "mail_address": "mododeveloper@gmail.com",
    #                "password": "password"
    #            }
    #        }
    #    }

    req = json.get("request")
    res = AuthorFacade.create(req)
    return jsonify(res)


@author_api.route("/author/read")
def read_author():
    json = {
        "request": {
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                }
        }
    }

    req = json.get("request")
    res = AuthorFacade.read(req)
    return jsonify(res)


@author_api.route("/author/update", methods=["POST"])
def update_author():
    json = {
        "request": {
            "credential": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "token": "b941295b36824f0fc19cc473ba9d6b67866b2709"
            },
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "author_name": u"Masahiro Atsumi desu!",
                "mail_address": "raindrop.aqua@gmail.com",
                "valid": True,
                }
        }
    }

    req = json.get("request")
    res = AuthorFacade.update(req)
    return jsonify(res)


@author_api.route("/author/update_password", methods=["GET", "POST"])
def update_password_author():
    json = {
        "request": {
            "credential": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "token": "b941295b36824f0fc19cc473ba9d6b67866b2709"
            },
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "password": "password"
            }
        }
    }

    req = json.get("request")
    res = AuthorFacade.update_password(req)
    return jsonify(res)


@author_api.route("/author/reset_password")
def reset_password_author():
    pass


@author_api.route("/author/authentication")
def authentication_author():
    json = {
        "request": {
            "substance": {
                "author_id": "a2e006bc0d489746ee6ac9415da7ef352091bbe8",
                "password": "password"
            }
        }
    }

    req = json.get("request")
    res = AuthorFacade.authentication(req)
    return jsonify(res)


@author_api.route("/author/list")
def list_author():
    res = AuthorFacade.list()
    return jsonify(res)
