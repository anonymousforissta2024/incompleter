#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
import peewee

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = peewee.MySQLDatabase(app).database

from comparteme import routes