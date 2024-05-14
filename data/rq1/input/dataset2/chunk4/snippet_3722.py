#Source: https://stackoverflow.com/questions/56689224/python-dict-datatype-error-while-after-reading-message-from-aws-sqs-and-put-it-i
import json
import boto3

dynamodb = boto3.resource('dynamodb')
dynamoTable = dynamodb.Table('message')

def lambda_handler(event, context):
    for record in event['Records']:
        data1 = record["body"]
        jsondata1 = json.loads(data1)
        print(jsondata1)
        dynamoTable.put_item(Item=jsondata1)      