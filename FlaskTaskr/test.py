import os
import unittest

from views import app, db
from _config import basedir
from models import User

TEST_DB = 'test.db'


class AllTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_setup(self):
        new_user = User('nipun', 'nipun@gmail.com', 'nipuns')
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == 'nipun'

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please sign in to access your task list',
                      response.data)

    def login(self, name, password):
        return self.app.post(
            '/',
            data=dict(name=name, password=password),
            follow_redirects=True)

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn(b'Invalid username or password', response.data)

    def register(self, name, email, password, confirm):
        return self.app.post(
            'register/',
            data=dict(
                name=name, email=email, password=password, confirm=confirm),
            follow_redirects=True)

    def test_users_can_login(self):
        self.register('npnsaddy', 'nipunsaddy@gmail.com', 'nipunsaddy',
                      'nipunsaddy')
        response = self.login('Nipun', 'nipunsaddy')
        self.assertIn(b'Welcome', response.data)

    def test_invalid_form_data(self):
        self.register('npnsaddy', 'nipunsaddy@gmail.com', 'nipunsaddy',
                      'nipunsaddy')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn(b'Invalid username or password', response.data)

    def test_form_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please register to access the task list.',
                      response.data)

    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register('npnsaddy', 'nipunsaddy@gmail.com',
                                 'nipunsaddy', 'nipunsaddy')
        self.assertIn(b'Thanks for registering. Please login.', response.data)

    def test_user_registration_error(self):
        self.app.get('register/', follow_redirects=True)
        response = self.register('npnsaddy', 'nipunsaddy@gmail.com',
                                 'nipunsaddy', 'nipunsaddy')
        self.app.get('register/', follow_redirects=True)
        response = self.register('npnsaddy', 'nipunsaddy@gmail.com',
                                 'nipunsaddy', 'nipunsaddy')
        self.assertIn(b'That username and/or email already exist.',
                      response.data)

    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    def test_logged_in_users_can_logout(self):
        self.register('Sadvilkar', 'sadvilkar@gmail.com', 'npnsadvilkar',
                      'npnsadvilkar')
        self.login('Sadvilkar', 'npnsadvilkar')
        response = self.logout()
        self.assertIn(b'Goodbye!', response.data)

    def test_not_logged_in_users_cannot_logout(self):
        response = self.logout()
        self.assertNotIn(b'Goodbye!', response.data)

    def test_logged_in_users_can_access_tasks_page(self):
        self.register('Sadvilkar', 'sadvilkar@gmail.com', 'npnsadvilkar',
                      'npnsadvilkar')
        self.login('Sadvilkar', 'npnsadvilkar')
        response = self.app.get('tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add a new task:', response.data)

    def test_not_logged_in_users_cannot_access_tasks_page(self):
        response = self.app.get('tasks/', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    def create_user(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post(
            'add/',
            data=dict(
                name='Go to the bank',
                due_date='2018-05-11',
                priority='1',
                posted_date='2018-05-10',
                status='1'),
            follow_redirects=True)

    def test_users_can_add_tasks(self):
        self.create_user('NipunSaddy', 'nipunsaddy@gmail.com',
                         'python')
        self.login('NipunSaddy', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(b'New entry was successfully posted. Thanks.',
                      response.data)

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user('NipunSaddy', 'nipunsaddy@gmail.com',
                         'python',)
        self.login('NipunSaddy', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.post(
                        'add/',
                        data=dict(
                            name='Go to the bank',
                            due_date='',
                            priority='1',
                            posted_date='2018-05-10',
                            status='1'),
                        follow_redirects=True)
        self.assertIn(b'This field is required.',
                      response.data)

    def test_users_can_complete_tasks(self):
        self.create_user('NipunSaddy', 'nipunsaddy@gmail.com',
                         'python')
        self.login('NipunSaddy', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('complete/1/', follow_redirects=True)
        self.assertIn(b'The task is complete. Nice', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user('NipunSaddy', 'nipunsaddy@gmail.com',
                         'python')
        self.login('NipunSaddy', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('delete/1/', follow_redirects=True)
        self.assertIn(b'The task was deleted.', response.data)

    def test_users_cannot_complete_tasks_that_are_not_created_by_them(self):
        self.create_user('NipunSaddy', 'nipunsaddy@gmail.com',
                         'python')
        self.login('NipunSaddy', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_user('Sadvilkar', 'sadvilkar@gmail.com',
                         'python')
        self.login('Sadvilkar', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('complete/1/', follow_redirects=True)
        self.assertNotIn(b'The task is complete. Nice.', response.data)

if __name__ == '__main__':
    unittest.main()
