# -*- coding: utf-8 -*-

from flask import Module

call_center_api = Module(__name__)

@call_center_api.route("/call_center/author_release_provisional/<token>")
def author_release_provisional_call_center(token):
    pass

@call_center_api.route("/call_center/forget_password")
def forget_password_call_center():
    pass

@call_center_api.route("/call_center/exists_forget_password_request/<token>")
def exists_forget_password_request_call_center(token):
    pass
