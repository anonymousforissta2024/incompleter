#Source: https://stackoverflow.com/questions/56035632/peewee-model-has-no-select-attribute-error
from peewee import *

db = SqliteDatabase('database/attendance.db')


class BaseModel:

    class Meta:
        database = db