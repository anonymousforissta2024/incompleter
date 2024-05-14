#Source: https://stackoverflow.com/questions/76435889/attributeerror-nonetype-object-has-no-attribute-encode-in-flask-app
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')
        account_type = request.form.get('account_type')

        #check if theres already an account using the provided email
        exist = User.query.filter_by(email=email).first()
        if exist:
            flash("Email already exists")
            return redirect('/login')

        # Hash the password before storing it in the database
        print(password)
        hashed_password = generate_password_hash(password)

        # Create a new User object
        user = User(first_name=first_name, last_name=last_name, email=email,
                    password=hashed_password, phone_number=phone_number, account_type=account_type)

        # Add the user to the database
        add_user(user)

        return redirect('/login')

    return render_template('html/signup.html')