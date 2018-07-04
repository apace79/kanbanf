# app.py

from flask import Flask

from kanbanf.config import add_config
from kanbanf.views import add_views
from kanbanf.cli import add_commands


def create_app(instance='dev'):
    this_app = Flask(__name__)

    add_config(this_app, instance)
    add_views(this_app)
    add_commands(this_app)

    return this_app
