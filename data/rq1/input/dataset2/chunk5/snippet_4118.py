#Source: https://stackoverflow.com/questions/72986198/policy-attribute-error-when-sending-email-by-smtp
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from PIL import Image
from io import BytesIO
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib


msg = MIMEMultipart("related")
msg['Subject'] = subject #time
msg['From'] = from_addr
msg['To'] = to_addr

html_output = "your html here"

msg.attach(MIMEText(html_output, "html"))

#plots is a dictionary of images

for image_name, image_location in plots.items():
   img = Image.open(BytesIO(image_location))
   msg.attach(img)
        
        
smtplib.SMTP(host).sendmail(from_addr, to_addr, msg.as_string())