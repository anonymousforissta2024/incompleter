#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from flask.ext.mongoalchemy import MongoAlchemy
from flask import Flask

mongododb = MongoAlchemy()

def init_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['MONGOALCHEMY_SERVER'] = 'localhost'
    app.config['MONGOALCHEMY_PORT'] = '27017'
    app.config['MONGOALCHEMY_DATABASE'] = 'publicvoicedb'
    mongododb.init_app(app)
    return app

class Location(mongododb.Document):
     type= mongododb.StringField()
     cooridantes =mongododb.StringField()


class Essential(mongododb.Document):
        subscriberName = mongododb.StringField()
        mobileNumber = mongododb.IntField()
        address = mongododb.StringField()
        pincode = mongododb.IntField()
        location = mongododb.DocumentField(Location)
        category = mongododb.StringField()
        request_date =mongododb.StringField()
        serviceType = mongododb.StringField() 
        issueDescription = mongododb.StringField()