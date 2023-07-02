from markupsafe import escape
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello World! Welcome to S14A2023</h1>'

@app.route('/datetime/')
def about():
    return '<h3>Server datetime: {}</h3>'.format(str(datetime.now()))

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])