#Source: https://stackoverflow.com/questions/56035632/peewee-model-has-no-select-attribute-error
from peewee import *
from models.basemodel import BaseModel


class Course(BaseModel):
    cid = PrimaryKeyField()
    title = TextField()
    active = BooleanField()

    class Meta:
        table_name = 'courses'