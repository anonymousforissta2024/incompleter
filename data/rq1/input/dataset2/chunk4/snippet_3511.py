#Source: https://stackoverflow.com/questions/63885766/python-error-typeerror-module-object-is-notcallable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
import pyAesCrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data-users2.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    pwd = db.Column(db.LargeBinary(), unique=True)

    def __init__(self, id, username, pwd):
        p = pyAesCrypt(encoding=False)
        self.id = id
        self.username = username
        self.pwd = p.encrypt("password",pwd)