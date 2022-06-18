# Import flask
from flask import Flask

# create flask instance named app
app = Flask(__name__)

# create app route
@app.route('/')
def hello_world():
    return 'Hello World'

# create a second route
@app.route('/one_piece')
def one_piece():
    return 'Does Exist!'