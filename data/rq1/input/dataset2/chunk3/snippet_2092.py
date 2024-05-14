#Source: https://stackoverflow.com/questions/33251130/python-3-import-typeerror-error
from myproject.app import app
from myproject.app import db

def create_tables():
    from myproject.models.util import Weekday, weekday_type
    from myproject.models.activity import Activity, activities_tags, Occurrence, Tag

    db.create_all()