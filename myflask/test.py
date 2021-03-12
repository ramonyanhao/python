from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/login')
def come():
   return 'welcome!'

@app.route('/reg')
def reg():
   return '注册'

if __name__ == '__main__':
   app.run(port=5050)