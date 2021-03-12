from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/login', methods=['GET'])
def signin_form():
    return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/login/world',methods=['GET'])
def world():
    return '''<form action="/login/hello" method="get">
    <p><button type="submit">登陆</button></p>
    </form>'''
@app.route('/login/hello',methods=['GET'])
def hello():
    return render_template('hello.html')

@app.route('/login', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    elif request.form['username']=='' and request.form['password']=='':
        return '<h3>没有用户</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()