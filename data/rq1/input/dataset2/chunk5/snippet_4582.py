#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# __init__.py

from flask import Flask
from config import Config
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL()
mysql.init_app(app)

from application import routes