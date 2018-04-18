from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

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
    app.run(debug=True)
