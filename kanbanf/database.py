# database.py
import sqlite3


def init(app):
    with sqlite3.connect(app.config['DATABASE']) as conn:
        with app.open_resource(app.config['SCHEMA'], mode='r') as f:
            conn.executescript(f.read())


def connection(app):
    return sqlite3.connect(app.config['DATABASE'])


def execute(app, stmt, data=(), pp=list):
    with connection(app) as conn:
        return pp(conn.execute(stmt, data))


def query(app, stmt, data=()):
    return execute(app, stmt, data)


class Projects():
    def __init__(self, app):
        self.table_name = 'projects'
        self.app = app

    def add(self, data):
        q = f'insert into {self.table_name} (name) values (?)'

        def get_lastrowid(c):
            return c.lastrowid

        execute()
        return conn.execute(self.app, q, select, data)

        # return execute(self.app, 'SELECT last_insert_rowid()')

    def get_all(self):
        return execute(self.app)
