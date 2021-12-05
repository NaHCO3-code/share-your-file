import os
from flask import (
    Flask, render_template, request
)
from gevent import pywsgi

# def create_app():
app = Flask(__name__)
app.config.from_mapping(
    DATABASE=os.path.join('./database', 'db.sqlite')
)

from database import database
database.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth/register')
def auth_register():
    return render_template('auth/register.html')

server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
server.serve_forever()

# return app