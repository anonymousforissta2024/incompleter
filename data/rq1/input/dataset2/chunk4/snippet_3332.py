#Source: https://stackoverflow.com/questions/70706978/loginmanager-typeerror-nonetype-object-is-not-callable
from flask import Flask
from flask_login import LoginManager
from .views import views
from .models import db,User
from flask_mobility import Mobility
from os import path

DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    Mobility(app)
    
    loginmanager=LoginManager(app)
    loginmanager.login_view('auth.login')

    app.config['SECRET_KEY']='no nothing nobody'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME):
        db.create_all(app=app)