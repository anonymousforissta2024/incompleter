#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from sqlalchemy.orm import relationship
from entities.utils import db
from entities.utils import utils

from sqlalchemy import Column, String, Integer, ForeignKey


class SessionModel(db.Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True,autoincrement=True)
    server = Column(String, nullable=False)
    world = Column(String,nullable=False)
    user = Column(String,nullable=False)
    version = Column(String,nullable=False)
    requests_id = Column(Integer, ForeignKey('requests.id'))
    requests = relationship('RequestModel')



    def __init__(self,server,world,user,version):
        self.server = server
        self.world = world
        self.user = user
        self.version = version



    def __repr__(self):
        return self._repr(id=self.id,server=self.server,
                          world=self.world,user=self.user,version=self.version)