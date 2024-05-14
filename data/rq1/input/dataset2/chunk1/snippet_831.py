#Source: https://stackoverflow.com/questions/64660868/lambda-error-typeerror-str-object-does-not-support-item-assignment-traceback
import json
import uuid
import boto3

def lambda_handler(event, context):
    
    dynamo_client = boto3.resource('dynamodb')
    loadeo_carrier_company = dynamo_client.Table('loadeo_carrier_company')
    
    
    item = {}
    item = event['body']
    print(item)
    item['company_id'] = str(uuid.uuid4())
    
    print (type(item))
    try:
        loadeo_carrier_company.put_item(
          
            Item=item
        )
        return {
            "statusCode": 200,
            "headers" : {
                "Access-Control-Allow-Origin" : "*"
            },
            "message": json.dumps("Record has been inserted"),
            "body": item
        }
    except Exception as e:
            return {
                "statusCode": 500,
                "headers" : {
                    "Access-Control-Allow-Origin" : "*"
                },
                "message": "Error: Unable to save record!"
            }
    