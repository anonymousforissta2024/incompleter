#Source: https://stackoverflow.com/questions/59919041/attributeerror-module-boto3-has-no-attribute-client-error-while-trying-to
import boto3
import json

client = boto3.client('lambda')

response = client.create_function(
Code={
},
Description='Test LambdaFunction using boto3 SDK',
FunctionName='TestLambda',
# is of the form of the name of your source file and then name of your function handler
Handler='lambda_function.lambda_handler',
MemorySize=128,
Publish=True,
# replace with the actual arn of the execution role you created
Role='arn:aws:iam::xxxxxxxxxx:role/TestRole',
Runtime='python3.7',
Timeout=15,
VpcConfig={
    'SubnetIds': [
        'subnet-xxxxxx',
        'subnet-xxxxxx'
    ],
    'SecurityGroupIds': [
        'sg-xxxxx66',
    ],
    'VpcId': 'vpc-xxxxx'
  },
)