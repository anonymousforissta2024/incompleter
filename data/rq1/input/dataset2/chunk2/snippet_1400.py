#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
import peewee
from comparteme import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(unique=True)