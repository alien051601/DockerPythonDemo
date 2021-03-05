from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/pic')
def show_picture():
    return render_template('index/index.html')


