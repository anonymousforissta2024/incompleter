#Source: https://stackoverflow.com/questions/57703151/typeerror-loads-got-an-unexpected-keyword-argument-max
@app.route('/email_confirm/<token>')
def confirm_mail(token):
    email = s.loads(token, salt='email-confirm', max_age=20)
    return '<h1>The token works !</h1>'