#Source: https://stackoverflow.com/questions/72377436/attributeerror-partially-initialized-module-boto3-has-no-attribute-session
import boto3
aws_mg_con=boto3.session.Session(profile_name='demo_user')
iam_con=aws_mg_con.resource('iam')