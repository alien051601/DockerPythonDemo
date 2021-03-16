from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/pic')
def show_picture():
    return render_template('index/index.html')


@app.route('/sea')
def show_png():
    return render_template('index/index_sea.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
