#Source: https://stackoverflow.com/questions/71804258/flask-app-nameerror-name-markup-is-not-defined
from flask import Flask, request, render_template, flash
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin
from flask_recaptcha import ReCaptcha
import requests
import json
import os

app = Flask(__name__, static_folder='static', static_url_path='')
recaptcha = ReCaptcha(app=app)

app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '***********************'
app.config['RECAPTCHA_PRIVATE_KEY'] = '****************************'

@app.route('/', methods=['GET'])
def index():
    return render_template("//index.html")

@app.route('/contact-us', methods=['GET'])
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data={'secret': '***********',
                                'response': request.form['g-recaptcha-response']})
        google_response = json.loads(r.text)

        if google_response['success']:
            contact_form = {'name': request.form['name'],
                            'email': request.form['email'],
                            'message': request.form['message']}
            msg = Message(subject='Contact from website',
                          sender=contact_form['email'],
                          recipients=['*************'],
                          body=contact_form['message'])
            mail.send(msg)
            flash('Success, we will respond within at least 24 hours.')
            return render_template('contact.html')

        else:
            flash('failed to submit, please retry or contact us at ************')
            return render_template('contact.html')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run()