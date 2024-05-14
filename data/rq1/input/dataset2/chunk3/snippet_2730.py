#Source: https://stackoverflow.com/questions/59425913/typeerror-object-of-type-location-is-not-json-serializable
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        login_user = mongo.db.mylogin
        existing_user = login_user.find_one({'email': request.form['email']})
        # final_location = geolocator.geocode(session['address'].encode('utf-8'))
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            login_user.insert({'name': request.form['username'], 'email': request.form['email'], 'password': hashpass, 'address': request.form['add'], 'location' : session['location'] })
            session['password'] = request.form['pass']
            session['username'] = request.form['username']
            session['address'] = request.form['add']
            session['location'] = geolocator.geocode(session['address'])
            flash(f"You are Registerd as {session['username']}")
            return redirect(url_for('home'))
        flash('Username is taken !')
        return redirect(url_for('home'))
    return render_template('index.html')