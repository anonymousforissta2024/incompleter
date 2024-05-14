#Source: https://stackoverflow.com/questions/68151863/getting-typeerror-nonetype-object-is-not-subscriptable-on-api-when-runing-cod
from flask import Flask, jsonify, request
from flask_cors import CORS
from icecream import ic

app = Flask(__name__)
CORS(app)

@app.route('/backend/signin', methods=['POST'])
def sign_in():
    data = request.json
    ic("*** app @ 53",data)
    return {"username": data['username'], "password":data["password"]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)