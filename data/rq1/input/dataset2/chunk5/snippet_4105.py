#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
            return render_template('err_login.html')
    return render_template('login.html', form=form)