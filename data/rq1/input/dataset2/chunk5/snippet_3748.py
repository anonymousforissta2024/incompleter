#Source: https://stackoverflow.com/questions/32908969/typeerror-str-does-not-support-the-buffer-interface-when-using-flask-sendmail
from flask.ext.sendmail import Message
from flask.ext.sendmail import Mail

mail = Mail()
mail.init_app(app)
msg = Message("Hello".encode('utf-8'), sender="xxx@xxx.com".encode('utf-8'), recipients="xxx@xxx.com".encode('utf-8'))
msg.body = "testing"
msg.html = "testing"
mail.send(msg)