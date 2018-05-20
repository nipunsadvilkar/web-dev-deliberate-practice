from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


# config
app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from flasktaskr.users.views import users_blueprint
from flasktaskr.tasks.views import tasks_blueprint

# register our blueprints

app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)
