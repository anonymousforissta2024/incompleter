#Source: https://stackoverflow.com/questions/60140174/basic-flask-app-not-running-typeerror-required-field-type-ignores-missing-fr
from flask import Flask, request, jsonify, abort, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'success': True,
        'index': 'Test Pass'
    })



if __name__ == '__main__':
    app.run(debug=True)