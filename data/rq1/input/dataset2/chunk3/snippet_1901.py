#Source: https://stackoverflow.com/questions/33251130/python-3-import-typeerror-error
from myproject.app import db
from myproject.models.enum import DeclEnum

class Weekday(DeclEnum):
    Sunday    = 'Sunday', {'offset': 0}
    Monday    = 'Monday', {'offset': 1}
    Tuesday   = 'Tuesday', {'offset': 2}
    Wednesday = 'Wednesday', {'offset': 3}
    Thursday  = 'Thursday', {'offset': 4}
    Friday    = 'Friday', {'offset': 5}
    Saturday  = 'Saturday', {'offset': 6}

weekday_type = Weekday.db_type(metadata=db.metadata)
weekday_type.register_with_psycopg(db.engine)