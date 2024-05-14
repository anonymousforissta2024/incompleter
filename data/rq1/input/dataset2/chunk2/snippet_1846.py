#Source: https://stackoverflow.com/questions/36865799/alembic-sqlalchemy-postgres-nameerror-name-string-is-not-defined-trying-to
from sqlalchemy import Column, String, Integer, DateTime
from serve_spec.db_global import db
import datetime
from time import time
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import ARRAY

class Issues(db.Base):

    __tablename__ = 'issues'

    id = Column(String, primary_key=True)
    thread_id                   = Column(String, nullable=False)
    created                     = Column(DateTime(timezone=False), nullable=False, default=datetime.datetime.utcnow)
    created_timestamp           = Column(Integer, nullable=False, default=time)
    created_by_user_name        = Column(String, nullable=False)
    is_parent                   = Column(Integer, nullable=False)
    parent_title                = Column(String)
    subscribed                  = Column(ARRAY(String))
    unsubscribed                = Column(ARRAY(String))
    pending_notifications_web   = Column(ARRAY(String))
    pending_notifications_email = Column(ARRAY(String))
    markdown_text               = Column(String, nullable=False, )
    kernel_id                   = Column(String, nullable=False)
    state                       = Column(String, nullable=False, default='open')
    labels                      = Column(JSON())