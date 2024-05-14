#Source: https://stackoverflow.com/questions/51384124/typeerror-mimetext-object-is-not-callable
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

msg = MIMEMultipart()

msg['Subject'] = 'Test message'
msg['From'] = sender
msg['To'] = row['email']
msg.attach = MIMEText(HTML_CONTENT, 'html')
filename = newFileName
attachment = open(newFileName, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)