#Source: https://stackoverflow.com/questions/72699297/python-flask-typeerror-not-supported-between-instances-of-nonetype-and
from flask import Flask, request, session
from flask_session import Session
from functools import wraps
from datetime import timedelta
from json import dumps
from rest.api import api, users_api, setups_api, reports
import os
import shutil


# App Instance
app = Flask(__name__)
project_path = os.path.abspath('.')
app.config['APPLICATION_ROOT'] = project_path
app.config['SESSION_COOKIE_PATH'] = project_path + "/cookies/"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.before_request
def make_session_permanent():
    app.permanent_session_lifetime = timedelta(hours=(5))
    if request.path not in ["/api/login", "/api/get-session-data"]:
        if not session.get('user'):
            return "Sign in needed.", 403


@app.route("/api/login", methods=["POST", ])
def login():
    # login things
    session['user'] = "whatever"
    return dumps("")


@app.route("/api/get-session-data")
def give_session_data():
    session_data = {
        "user": session.get("user")
    }
    return dumps(session_data)