#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
import os                            

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-know'
    DATABASE = {
        'name': 'comparteme',                        
        'engine': 'peewee.MySQLDatabase',            
        'user': 'root',
        'password': 'whatever',                
        'host': os.environ.get('DATABASE_URL') or 'mysql://root@localhost:3306'
    }