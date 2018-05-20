import os
import unittest

from flasktaskr import app, db
from flasktaskr._config import basedir
from flasktaskr.models import User

TEST_DB = 'test.db'


class MainTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()
        self.assertEquals(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ########################
    #### helper methods ####
    ########################

    def login(self, name, password):
        return self.app.post(
            '/',
            data=dict(name=name, password=password),
            follow_redirects=True)

    def test_404_error(self):
        response = self.app.get('/unknown-route/')
        self.assertEquals(response.status_code, 404)
        self.assertIn(b'Sorry. there\'s nothing here.', response.data)

    def test_500_error(self):
        bad_user = User(name='abcde',
                        email='abcd@abcd.com',
                        password='qwerty')
        db.session.add(bad_user)
        db.session.commit()
        response = self.login('adcde', 'qwerty')
        self.assertEquals(response.status_code, 500)
        self.assertNotIn(b'ValueError: Invalid salt', response.data)
        self.assertIn(b'Somethingg went terribly wrong', response.data)


if __name__ == '__main__':
    unittest.main()
