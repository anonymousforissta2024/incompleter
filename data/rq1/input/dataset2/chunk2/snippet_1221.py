#Source: https://stackoverflow.com/questions/63900355/flaskflask-db-init-attributeerror-module-time-has-no-attribute-clock
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))   #Full directory path of the file I'm working with..here, sql1.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

Migrate(app,db) #Here it connect the application "app.py"
                # with the database "db"    
class puppy(db.Model):
    __tablename__ = 'Name Provided by me!!'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"puppy {self.name} is {self.age} year/s old!"