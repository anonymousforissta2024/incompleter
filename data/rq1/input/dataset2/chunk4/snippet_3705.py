#Source: https://stackoverflow.com/questions/57734727/typeerror-argument-of-type-mail-is-not-iterable
@app.route('/email', methods=['GET', 'POST'])
def send_mail():
    getting = request.form.get('mail')
    token = s.dumps(getting, salt='email-confirm')

    msg = Message('Confirm Email', sender='vatsalayvk1434@gmail.com', recipients=[mail])

    link = url_for('confirm_mail', token=token, _externel=True)
    msg.body = f'Your Link is {link}'

    mail.send(msg)
    return render_template('confirm.html', getting=getting, token=token)