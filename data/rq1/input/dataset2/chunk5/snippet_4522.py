#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# config.py

import os
from flask_mysql_connector import MySQL

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'djfdsjdsj4skldjess85'

    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'flasker'
    MYSQL_DATABASE_PASSWORD = '**********'
    MYSQL_DATABASE_DB = 'UTA_Enrollment'