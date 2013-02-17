# -*- coding: utf-8 -*-

from flask import Flask
from application.handlers.api.author import author_api
from application.handlers.api.kit import kit_api
from application.handlers.api.call_center import call_center_api
from application.handlers.api.category import category_api

app = Flask(__name__)
app.register_module(author_api)
app.register_module(kit_api)
app.register_module(call_center_api)
app.register_module(category_api)

if __name__ == "__main__":
    app.run()
