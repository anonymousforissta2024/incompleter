#Source: https://stackoverflow.com/questions/59012381/pytest-flask-application-attributeerror-module-src-api-has-no-attribute-test
from flask import Flask, jsonify


api = Flask(__name__)


@api.route('/')
def hello_world():
    return jsonify(message="hello world")


if __name__ == '__main__':
    api.run(debug=True)