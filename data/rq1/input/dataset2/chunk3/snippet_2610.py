#Source: https://stackoverflow.com/questions/57184677/attributeerror-module-yagmail-has-no-attribute-smtp
import yagmail
receiver = "pat*******@gmail.com"
body = "Hello there from Yagmail"
filename = "c.pdf"

yag = yagmail(user="dar**********@gmail.com", password="**********", host='smtp.gmail.com')
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)