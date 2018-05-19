import os

# folder path where this script resides
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x06\x14\xd8\xab\x9f\x80\x9e\x98\x8e\xe8\xf3\xfd\xa0\x89'

# full path to Database
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
