#Source: https://stackoverflow.com/questions/69659778/handlerlambda-handler-missing-on-module-lambda-function-errortype-run
import boto3
from datetime import datetime, timedelta
from dateutil.tz import tzutc, UTC

BUCKET = 'my-bucket'
TOPIC_ARN = 'arn:aws:sns:ap-southeast-2:123456789012:Old-File-Warning'

s3_resource = boto3.resource('s3')
sns_resource = boto3.resource('sns')
sns_topic = sns_resource.Topic(TOPIC_ARN)

for object in s3_resource.Bucket(BUCKET).objects.filter(Prefix='folder1/folder2/'):
    if object.last_modified > datetime.now(tzutc()) - timedelta(hours = 1):
        message = f"Object {object.key} is more than 1 hour old!"
        sns_topic.publish(Message=message)