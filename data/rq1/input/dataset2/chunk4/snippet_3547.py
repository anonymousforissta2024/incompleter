#Source: https://stackoverflow.com/questions/37783437/nameerror-which-isnt-name-error-python
#!/usr/bin/python
import os
import smtplib
with open("/linux/sendmail",'r') as nas_file:
    success=nas_file.read()

print(success)
def send_mail(msg):
    fromaddr = 'XXXXX'
    toaddrs  = 'XXXXX'


    # Credentials (if needed)
    username = 'XXXXX'
    password = 'XXXXX'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return
if True:
    send_mail(success)