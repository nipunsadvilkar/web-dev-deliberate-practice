from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import datetime


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
def page_not_found(error):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime('%d-%m-%Y %H:%M:%S')
            f.write("\n404 error at {}: {}".format(current_timestamp, r))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime('%d-%m-%Y %H:%M:%S')
            f.write("\n500 error at {}: {}".format(current_timestamp, r))
    return render_template('500.html'), 500
