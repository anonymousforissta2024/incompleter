#Source: https://stackoverflow.com/questions/72941940/attributeerror-list-object-has-no-attribute-split-boto3
import boto3
account_id = 'accountID'
role_name = 'MyRole'

def assume_role(role_name, account_id):
    session = boto3.Session()
    sts_client = session.client('sts')
    assumed_role_object = sts_client.assume_role(
        RoleArn=f'arn:aws:iam::{account_id}:role/{role_name}',
        RoleSessionName = f'{role_name}-Session'
    )

    assumed_role_credentials = assumed_role_object['Credentials']

    assumed_session = boto3.Session(
        aws_access_key_id=assumed_role_credentials['AccessKeyId'],
        aws_secret_access_key=assumed_role_credentials['SecretAccessKey'],
        aws_session_token=['SessionToken']
    )
    return assumed_session

ec2_role_session = assume_role(role_name, account_id)
instances = ec2_role_session.resource('ec2', region_name="us-east-1").instances.all()

for instance in instances:
    print(f"Instance ID: {instance.id}")