from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! By Flask GTO'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
