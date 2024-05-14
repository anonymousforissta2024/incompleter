#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from database.db import mongododb
from database.db import Location
from database.db import Essential

def create_essential_service(data):
    print('data =', data)
    essentialData = Essential(subscriberName=data['subscriberName'],
    mobileNumber=data['mobileNumber'])

    essentialData.save()


def get_all_service():
    return Essential.query.filter(Essential.serviceType == 'PoliceService').first()

def get_by_service_type(serviceType):
    return Essential.query.filter_by(serviceType=serviceType).first()