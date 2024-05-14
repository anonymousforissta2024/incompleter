#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.create_all()
        db.session.add(new_user)
        db.session.commit()
        return render_template('register_ok.html', form=form)
    return render_template('register.html', form=form)