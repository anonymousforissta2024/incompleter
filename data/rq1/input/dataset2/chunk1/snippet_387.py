#Source: https://stackoverflow.com/questions/51391849/typeerror-resultproxy-object-does-not-support-indexing-when-trying-to-store-u
@app.route("/signin",methods=["GET","POST"])
def signin():
    # LOG A USER IN
    #forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    else:
        user_name = request.form.get("username")

        # ensure username is provided
        if not request.form.get("username"):
            return "must provide username"

        # ensure password is provided
        elif not request.form.get("password"):
            return "must provide password"


        # query the database for the username
        rows = db.execute("SELECT * FROM users where username = :username",{"username":user_name})

        # ensure username exists 
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"),rows[0]["hash"]):
            return "Invalid username"

        # remember which user has logged in 
        session["user_id"] = rows[0]["id"]