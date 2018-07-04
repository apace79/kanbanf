# cli.py

from kanbanf import database as db


def add_commands(app):
    @app.cli.command()
    def initdb():
        """Initializes the database."""
        db.init(app)
        print('Initialized the database.')
