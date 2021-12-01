import re
from flask import (
    Flask, render_template, request
)
from gevent import pywsgi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/auth/login', methods=('GET', 'POST'))
def auth_login():
    if request.method == 'POST':
        pass
    return render_template('/auth/login.html')

server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
server.serve_forever()