#Source: https://stackoverflow.com/questions/63123537/aws-ssm-python-boto3-create-hybrid-activation-expirationdate-type-error
import boto3
import datetime

client = boto3.client('ssm')
current_date = datetime.date.today()
creation_date = current_date.strftime('%Y%m%d')
end_date = current_date + datetime.timedelta(days=30)
y = end_date.year
m = end_date.month
d = end_date.day
divisions = ['div1', 'div2', 'div3']

#def lambda_handler(event, context):

for x in divisions:
    client.create_activation(
        Description = (x + '-' + 'creation_date'),
        #DefaultInstanceName = 'string',
        IamRole = 'MySSMServiceRole',
        RegistrationLimit = 200,
        ExpirationDate = datetime(y, m, d),
        Tags=[
            {
                'Key': 'Division',
                'Value': x
            },
        ]
    )
    print('\n ' + x + '-creation_date was create.')