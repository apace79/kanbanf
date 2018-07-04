# views.py
from flask import jsonify


def add_views(app):
    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route("/projects/")
    def project():
        return jsonify({'projects': [{'id': 1, 'name': 'KANBAN'},
                                     {'id': 2, 'name': 'REACT'},
                                     {'id': 3, 'name': 'BOARDGAME'}]})


# @app.route("/projects/")
#   POST


# @app.route("/projects/<project_id>")
# def project(project_id):
#    return project_id
