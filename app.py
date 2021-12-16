from abc import update_abstractmethods
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
app.secret_key = 'dev'

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
        # 获取表单
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        db = database.get_db()
        errors = None

        # 校验信息
        if not username:
            errors = "请输入用户名。"
        if not password or len(password)<=6:
            errors = "请输入不少于六位的密码。"
        if password != password2:
            errors = "前后密码不一致。请重试。"

        # 注册用户
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

        # 发送错误信息
        if errors:
            return render_template('auth/register.html', error=errors)

        #注册成功并创建session
        flask.session.clear()
        flask.session['username'] = username
        flask.session['password'] = password
        return '<a href="/" id="a">登陆成功!去首页</a><script>setInterval(()=>{document.getElementById("a").click()},500)</script>'

    return render_template('auth/register.html')

@app.route('/auth/login', methods=('GET', 'POST'))
def auth_login():
    if request.method == 'POST':
        # 获取表单
        username = request.form.get('username')
        password = request.form.get('password')
        db = database.get_db()
        errors = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        # 校验信息
        if not user:
            errors = '用户不存在！'
        elif user['password'] != password:
            errors = '密码错误！'+user['password']+" "+password
        if errors == None:
            flask.session.clear()
            flask.session['username'] = username
            flask.session['password'] = password
            return '<a href="/" id="a">登陆成功!去首页</a><script>setInterval(()=>{document.getElementById("a").click()},500)</script>'
        
        return render_template('auth/login.html', error=errors)

    return render_template('auth/login.html')









# server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
# server.serve_forever()
if __name__ == "__main__": app.run(host='0.0.0.0', port='5000')
