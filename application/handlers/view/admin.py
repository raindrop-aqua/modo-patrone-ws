# -*- coding: utf-8 -*-

from flask import Module, render_template

admin_view = Module(__name__)


@admin_view.route("/admin")
def admin_menu():
    return render_template("index.html")


