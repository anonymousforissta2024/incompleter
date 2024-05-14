#Source: https://stackoverflow.com/questions/58803820/unable-to-attach-excel-file-to-email-using-python-typeerror-expected-bytes-li
import boto3
import xlsxwriter
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def lambda_handler(event, context):
    client = boto3.client('ses',region_name=AWS_REGION)
    sender = "xxx@gmail.com"
    to = "aaa@gmail.com"
    workbook = xlsxwriter.Workbook('abc.xlsx') 
    worksheet = workbook.add_worksheet() 
    worksheet.write('A1', 'Hello..')
    #send email with attachment
    msg = MIMEMultipart()
    msg['Subject'] = 'Test Email'
    msg['From'] = sender
    msg['To'] = to
    body_text = MIMEText(BODY_TEXT, "html")
    attachment = MIMEApplication(workbook)
    attachment.add_header('Content-Disposition', 'attachment', filename='Expenses01.xlsx')
    msg.attach(attachment)
    msg.attach(body_text)
    response = client.send_raw_email(
        Source=sender,
        Destinations=[to],
        RawMessage={"Data": msg.as_string()}

    )