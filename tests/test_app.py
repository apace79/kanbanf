import unittest
import os
import tempfile
import string
import random

from flask import json
from kanbanf.app import create_app
from kanbanf import database as db


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True

    def test_schema(self):
        self.assertEqual(self.app.config['SCHEMA'], 'schema.sql')

    def test_database(self):
        self.assertEqual(self.app.config['DATABASE'], 'instance/dev.db')


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.db_fd, self.app.config['DATABASE'] = tempfile.mkstemp()
        print(self.app.config['DATABASE'])
        db.init(self.app)

    def tearDown(self):
        if os.path.isfile(self.app.config['DATABASE']):
            os.close(self.db_fd)
            os.remove(self.app.config['DATABASE'])

    def test_empty_projects(self):
        with db.execute(self.app, 'select * from projects') as c:
            self.assertIsNone(c.fetchone())

    def test_add_projects(self):
        p = db.Projects(self.app)
        name = ''.join(random.choices(string.ascii_uppercase, k=6))
        id = p.add((name,))
        c = db.execute(self.app, 'select * from projects')
        self.assertEqual((id, name), c[0])

    def test_get_projects(self):
        p = db.Projects(self.app)
        name = ''.join(random.choices(string.ascii_uppercase, k=6))
        id = p.add((name,))
        ps = p.get_all()
        self.assertEqual(len(ps), 1)
        self.assertIn((id, name), ps)
        name2 = ''.join(random.choices(string.ascii_uppercase, k=6))
        id2 = p.add((name2,))
        ps = p.get_all()
        self.assertEqual(len(ps), 2)
        self.assertIn((id, name), ps)
        self.assertIn((id2, name2), ps)


class APITests(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        db.init(app)

    def tearDown(self):
        os.close(self.db_fd)
        os.remove(app.config['DATABASE'])

    def test_index(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_empty_projects(self):
        response = self.app.get('/projects/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8').rstrip(),
                         json.dumps(dict()))

    def test_create_project(self):
        pass

    def test_get_one_project(self):
        test_dict = {'name': 'test'}
        # insert_project(self.app, test_dict)
        response = self.app.get('/projects/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8').rstrip(),
                         json.dumps(test_dict))


if __name__ == '__main__':
    unittest.main()
