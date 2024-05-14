#Source: https://stackoverflow.com/questions/55708257/flask-attributeerror-module-object-has-no-attribute-app
import os
import click

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import flask_lab.tmp.test.demo

app = Flask(__name__)
prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
db = SQLAlchemy(app)

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(20))

flask_lab.tmp.test.demo()