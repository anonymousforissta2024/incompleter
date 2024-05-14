#Source: https://stackoverflow.com/questions/56242706/flask-bcrypt-check-password-method-always-return-type-error
@app.route('/sign_up' , methods=['POST', 'GET'])
def sign_up():
    form = register_form() # imported from forms.py file as a class
    db.connect()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        cur.execute("SELECT email FROM users WHERE email ='%s'", (email))
        email_exsist = cur.fetchone()
        if email_exsist:

            flash ('email is already exisist','danger')
        else :    

            cur.execute('INSERT INTO users(first_name, last_name,email,password) VALUES(%s,%s,%s,%s)''',(first_name, last_name, email, hashed_password) )
            db.commit()
            flash(f'Account Successfully created for {form.first_name.data + " " + form.last_name.data} !' , 'success' )

            return redirect(url_for('sign_up'))
            cur.close()

    return render_template('sign_up.html' , title='Sign up' , form= form)