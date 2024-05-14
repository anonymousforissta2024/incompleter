#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from sqlalchemy.orm import relationship, declarative_base
from entities.utils import db
from entities.utils.utils import _repr

from sqlalchemy import Column, JSON, INTEGER, ForeignKey, Integer


class ResponseModel(db.Base):

    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, autoincrement=True)

    headers = Column(JSON, nullable=False)
    status_code = Column(INTEGER, nullable=False)
    body = Column(JSON, nullable=True)


    def __init__(self, headers, status_code, body):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return self._repr(id=self.id, status=self.status_code)