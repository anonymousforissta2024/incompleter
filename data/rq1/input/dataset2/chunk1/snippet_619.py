#Source: https://stackoverflow.com/questions/46111203/flask-dynamo-connection-issueattributeerror-dynamo-object-has-no-attribute
from flask import Flask
from flask_dynamo import Dynamo
import os
os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''
os.environ['AWS_REGION'] = 'ap-south-1'
app = Flask(__name__)
app.config['DYNAMO_TABLES'] = [
{
    'TableName': 'users',
    'KeySchema': [dict(AttributeName='username', KeyType='HASH')],
    'AttributeDefinitions': [dict(AttributeName='username', AttributeType='S')],
    'ProvisionedThroughput': dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
}, {
     'TableName': 'groups',
    'KeySchema': [dict(AttributeName='name', KeyType='HASH')],
    'AttributeDefinitions': [dict(AttributeName='name', AttributeType='S')],
    'ProvisionedThroughput': dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
}
      ]
app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 9000
dynamo = Dynamo()