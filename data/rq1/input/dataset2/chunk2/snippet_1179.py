#Source: https://stackoverflow.com/questions/59207486/flask-render-template-not-working-typeerror-nonetype-object-is-not-iterabl
@app.route("/login", methods=["GET", "POST"])
def login_route():
    print("in login route")
    form = LoginForm()
    if "logged_in" in session:
        print("found in sesstion")
        return redirect(url_for("index_route"))

    if form.validate_on_submit():
        print("FORM VALID")
        feadback = val_login(form.username, form.password)
        print(feadback)
        if feadback[0] == 1:  # correct usr/psw
            print("got through if")
            agent = request.user_agent.string
            time = get_time()
            newHistory = LoginHistory(usr_id=int(feadback[1]), time=time, device_type=agent)
            db.session.add(newHistory)
            db.session.commit()
            session["logged_in"] = True
            print(session["logged_in"])
            session["username"] = feadback[3]
            session["id"] = feadback[1]
            if feadback[2]:
                session["admin"] = True

            return redirect(url_for("index_route"))
        else:
            print("error")
            return render_template("login.html", form=form, error="true")
    print("at render")
    return render_template("login.html", form=form)