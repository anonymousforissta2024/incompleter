#Source: https://stackoverflow.com/questions/56242706/flask-bcrypt-check-password-method-always-return-type-error
@app.route('/login' , methods=['POST', 'GET'])
def login():
    form = login_form()# imported from forms.py file as a class
    email = form.email.data
    if form.validate_on_submit():
        cur.execute("SELECT email FROM users WHERE email =%s", [email])
        user_email = cur.fetchone()
        cur.execute("SELECT password FROM users WHERE email =%s",[email])
        hashed_password = cur.fetchone()
        if user_email and bcrypt.check_password_hash( hashed_password,form.password.data) :
            login_user(user_email,remember=form.remember.data)
            return redirect(url_for('home'))
        else :
            flash ('Unable to log in , please check your email and password', 'danger')

    return render_template('login.html' , title='login' , form= form)