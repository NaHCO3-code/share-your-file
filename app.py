import os
from flask import (
    Flask, render_template, request
)
from gevent import pywsgi
import execjs



# app初始化
app = Flask(__name__)
app.config.from_mapping(
    DATABASE=os.path.join('./database', 'db.sqlite')
)

# 定义数据库
from database import database
database.init_app(app)

# # MD5加密
# md5_js = execjs.compile(open('./static/js/md5.js', 'r', encoding='utf=8'))



# 路由
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth/register')
def auth_register():
    return render_template('auth/register.html')

@app.route('/auth/login', methods=('GET', 'POST'))
def auth_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        return str([username,password,password2])

    
    return "awa?"

server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
server.serve_forever()
