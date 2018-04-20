"""Exploring basic functionality of flask framework"""
# import Flask class from flask module
from flask import Flask

# Instantiate app with Flask class
# create the application object
app = Flask(__name__)

# error handling
app.config['DEBUG'] = True

# using decorators to link function to a url
@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# dynamic route
@app.route('/test/<search_query>')
def search_with_query(search_query):
    return search_query

# dynamic route with converter variable rules
# <converter:variable_name>
# integer converter
@app.route('/int/<int:int_val>')
def give_int(int_val):
    return 'Integer given is {0}'.format(int_val)

# float converter
@app.route('/float/<float:float_val>')
def give_float(float_val):
    return 'Float given is {0}'.format(float_val)

# dynamic route that accepts slashes
@app.route('/path/<path:path_val>')
def give_some_path(path_val):
    return 'Path given is {0}'.format(path_val)

# dynamic route with explicit status codes
@app.route('/name/<name>')
def whoami(name):
    if name.lower() == 'nipun':
        return 'You Rock, {}!'.format(name), 200
        # even if you remove 2nd param - 200 - "OK" status code Flask is so
        # smart that it will return same Status Code 200 and Content-Type of
        # "text/html". But best practice is to return Status Code
        # since client side behavior (front-end) is often dependent on them
    else:
        return "Sorry {}, You're not allowed!".format(name), 404

# you can make the file usable as a script as well as an importable module,
# if the module is executed as the “main” file [through command line like
# `$ python filename.py`] then following lines will get
# executed since global or special varibale called __name__ will be set to
# __main__ and if it's imported then __name__ is set to 'filename'
# this modules [filename].py
# for more details:
# 1. https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# 2. http://ibiblio.org/g2swap/byteofpython/read/module-name.html
if __name__ == '__main__':
    # start development server with run method
    app.run()

