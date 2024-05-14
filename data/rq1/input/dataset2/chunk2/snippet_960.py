#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import datetime
from entities.models.Request import RequestModel
from entities.models.Response import ResponseModel
from entities.models.Session import SessionModel





engine = create_engine('postgresql://XXX:XXX@localhost:5423/XXXX')
Base = declarative_base()
# create session and add objects
with Session(engine) as session:
    response_object = ResponseModel(body={'22':'22'},status_code=402,headers={'test':'test'})
    session.add(response_object)
    session.commit()

    object_1 = RequestModel('POST', 402, 'www.intersecting.com/url?=parameter1&key')
    object_1.headers = {'test':'19'}
    object_1.body = {'test':'19'}
    object_1.size = 512
    object_1.timestamp_start = datetime.datetime.now()
    object_1.timestamp_end =datetime.datetime.now()
    object_2 = object_1
    session.add(object_1)
    session.commit()
    session_object = SessionModel('www.test.com','test62','admin','3.12.13')
    print(session_object)
    session_object.requests = {object_2,object_1}
    session.add(session_object)
    session.commit()