from markupsafe import escape
from datetime import datetime, timezone, timedelta
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello World! Welcome to S14A2023</h1>'

@app.route('/datetime/')
def dt():
    cst_offset = timedelta(hours=-5)
    return '<h3>Server datetime: {}<br>UTC datetime: {}<br> Aneesh\'s (Dallas, TX) datetime: {}</h3>'.format(
        str(datetime.now()), str(datetime.now(timezone.utc)), str((datetime.now(timezone.utc) + cst_offset)))