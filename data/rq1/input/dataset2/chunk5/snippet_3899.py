#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from flask import Flask, jsonify, request, json
import psycopg2
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__)
conn = psycopg2.connect(host="localhost", database="practise",
                        user="postgres", password="dbA@pr3mium")
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

import login