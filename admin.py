# -*- coding: utf-8 -*-

from flask import Flask
from application.handlers.view.admin import admin_view
from application.handlers.view.author import author_view
from application.handlers.view.kit import kit_view
from application.handlers.view.category import category_view
from jinja2 import FileSystemLoader

app = Flask(__name__)

app.jinja_loader = FileSystemLoader("application/templates")
app.register_module(admin_view)
app.register_module(author_view)
app.register_module(kit_view)
#app.register_module(call_center_api)
app.register_module(category_view)

if __name__ == "__main__":
    app.run()
