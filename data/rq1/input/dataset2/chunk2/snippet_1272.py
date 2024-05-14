#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from sqlalchemy.orm import relationship
from entities.utils import db
from entities.utils.utils import _repr

from sqlalchemy import Column, String, JSON, INTEGER, ForeignKey, Integer, DateTime


class RequestModel(db.Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True,autoincrement=True)
    headers = Column(JSON,nullable=False)
    method = Column(String,nullable=False)
    size = Column(INTEGER,nullable=False)
    timestamp_end = Column(DateTime,nullable=False)
    timestamp_start = Column(DateTime,nullable=False)
    status_code = Column(INTEGER,nullable=False)
    body = Column(JSON,nullable=True)
    url = Column(String,nullable=False)



    response_id =  Column(INTEGER,ForeignKey('responses.id'))


    def __init__(self,method,status_code,url):
        self.method = method
        self.status_code = status_code
        self.url = url