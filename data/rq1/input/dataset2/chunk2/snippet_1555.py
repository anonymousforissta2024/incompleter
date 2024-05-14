#Source: https://stackoverflow.com/questions/54570871/attributeerror-sqlalchemy-object-has-no-attribute-integer
from datetime import datetime
from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)    #name of the module
app.config['SECRET_KEY']= 'b2ffa54db1c495dab1f21973b39c400a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =  SQLAlchemy(app)


class User(db.Model):
    id = db.column(db.integer, primary_key=True)
    username = db.column(db.string(25), unique=True, 
nullable=False)
    email = db.column(db.string(100), unique=True, nullable=False)
    password = db.column(db.string(100), unique=True, 
nullable=False)
    image_file = db.column(db.string(20), nullable=False, 
default='default.jpg')
    posts = db.relationship('Post', backreff='author', lazy=True)


    def __repr__(self):
       return f"user('{self.username}','{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.column(db.integer, primary_key=True)
    title = db.column(db.String(120), nullable=False)
    date_posted = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.column(db.Text, nullable=False)

def __repr__(self):
       return f"post('{self.title}','{self.date_posted}')"