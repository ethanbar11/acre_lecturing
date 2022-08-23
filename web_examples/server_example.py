from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return '<h1>yes!</h1>'


@app.route('/bla/<user>')
def print_user(user):
    return 'Your user name is {}'.format(user)


@app.route('/')
def random_number():
    return str(random.randint(1, 10))


@app.route('/something', methods=['POST'])
def something():
    d = request.get_json()
    d['bla'] = 'bla bla'
    return jsonify(d)


if __name__ == '__main__':
    app.run()
