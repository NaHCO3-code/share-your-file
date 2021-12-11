import os,time,random
import re
import flask
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

@app.route('/auth/register', methods=('GET', 'POST'))
def auth_register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        db = database.get_db()
        errors = None
        if not username:
            errors = "请输入用户名。"
        if not password or len(password)<=6:
            errors = "请输入不少于六位的密码。"
        if password != password2:
            errors = "前后密码不一致。请重试。"

        try:
            db.execute(
                "INSERT INTO user (id,username,password,class,jointime) VALUES (?,?,?,?,?)",
                (
                    int(str(random.randint(10,99))+str(int(time.time()*1000))),
                    username,
                    password,
                    'peo',
                    str(time.time())
                )
            )
            db.commit()
        except db.IntegrityError:
            errors = "用户已存在！请重试！"

        if errors:
            return render_template('auth/register.html', error=errors)
        return flask.redirect('/auth/login')
    
    return render_template('auth/register.html')

@app.route('/auth/login', methods=('GET', 'POST'))
def auth_login():
    return "awa?"






# server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
# server.serve_forever()
if __name__ == "__main__": app.run('0.0.0.0', '5000')
