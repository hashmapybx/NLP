from flask import Flask
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app=app)

@app.route('/')
def hello_world():
    a = 10
    b = 0
    c = a /b
    print(c)
    return '<h1>今天居然下雨了</h1>'


if __name__ == '__main__':
    manager.run()
