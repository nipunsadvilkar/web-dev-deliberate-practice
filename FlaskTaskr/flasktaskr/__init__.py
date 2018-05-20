from flask import Flask, render_template
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


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
