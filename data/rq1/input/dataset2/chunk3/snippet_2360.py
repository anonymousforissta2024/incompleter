#Source: https://stackoverflow.com/questions/55813036/how-to-solve-the-error-typeerror-a-bytes-like-object-is-required-not-str-wi
from threading import Thread
from flask_mail import Message
from app import app, mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    with app.open_resource("../logs/chaos.log") as fp:
        msg.attach(b'../logs/chaos.log', fp.read())
    Thread(target=send_async_email, args=(app, msg)).start()