#Source: https://stackoverflow.com/questions/77539653/exception-raised-in-application-typeerror-nonetype-object-is-not-subscriptab
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Main variables
    user_id = session["user_id"]
    user_cash = db.execute("SELECT cash FROM users WHERE id == ?", user_id)[0]["cash"]
    counter = 0
    shares_total = 0
    user_info = db.execute("SELECT user_id, symbol, SUM(shares) as shares, price, total, MAX(timestamp) as timestamp FROM info WHERE user_id == ? AND shares > 0 GROUP BY symbol", user_id)
    counter = len(user_info)

    # MAIN calculation loop
    if counter != 0:
        for j in range(1):
            for i in range(counter):

                symbol = user_info[i]["symbol"]
                price = lookup(symbol)["price"]
                total = price * user_info[i]["shares"]
                cash = user_cash - total

                # This if statement means if there is more symbol and shares the do this
                if counter > 1:
                    shares_total += user_info[i]["total"]

                elif counter == 1:
                    shares_total = user_info[i]["total"]

                db.execute("UPDATE info SET price == ?, total == ? WHERE user_id == ? AND symbol == ?", price, total, user_id, symbol)

            # Select current cash and then incriment
            cash = db.execute("SELECT cash FROM users WHERE id == ?", user_id)[0]["cash"]
            main_total = cash + shares_total

        return render_template("layout.html", user_info = user_info, i=i, counter = counter, total = total, price = price, tottal = main_total, cash = cash)

    else:

        return render_template("layout.html", cash = user_cash, tottal = user_cash, counter = counter)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""


    if request.method == "GET":
        return render_template("buy.html")

    else:

        user_id = session["user_id"]
        input_shares = request.form.get("shares")
        cash = db.execute("SELECT cash FROM users WHERE id == ?", user_id)[0]["cash"]


        # Erro hendling statements
        try:
            input_shares = int(request.form.get("shares"))

        except ValueError:
            return apology("shares must be a posative integer", 400)

        input_shares = int(input_shares)

        if input_shares <= 0:
            return apology("Shares number should be more then 0")

        if lookup(request.form.get("symbol")) is None:
            return apology("Please enter valid quotes")

        price = lookup(request.form.get("symbol"))["price"]

        if cash < price * input_shares:
            return apology("You don't have enough money")

        symbol = lookup(request.form.get("symbol"))["name"]
        shares = db.execute("SELECT shares FROM info WHERE user_id == ? AND symbol == ?", user_id, symbol)

        # This statemen is for error hendling, it's neccesery because if there is no purchase yet
        # It will purchase some shares and then return
        if len(shares) == 0:

            total = price * input_shares
            cash -= total
            db.execute("UPDATE users SET cash == ? WHERE id == ?", cash, user_id)
            db.execute("INSERT INTO info (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)", user_id, symbol, input_shares, price, total)
            db.execute("INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, symbol, input_shares, price)

            flash('You have bought!', 'success')
            return redirect("/")

        elif len(shares) > 0:

            # ar dagaviwydes rom sheamowmo len(shares) im shemtxvevashi tu ki romelime stock bevri yidva gayidvis istoria aqvs
            # da unda vnaxot ramdenad sworad gvichvenebs shares[0]["shares"] tavis monacems!!!!!!!!!!!!!!!!!!!!!!!!!

            shares = db.execute("SELECT shares FROM info WHERE user_id == ? AND symbol == ?", user_id, symbol)
            shares = shares[0]["shares"]

            shares += input_shares

            # Calculate and then Update all of the information into a SQL database
            total = price * shares

            cash = cash - price * input_shares

            db.execute("UPDATE users SET cash == ? WHERE id == ?", cash, user_id)
            db.execute("UPDATE info SET symbol == ?, price == ?, shares == ?, total == ? WHERE user_id == ? AND symbol == ?", symbol, price, shares, total, user_id, symbol)
            db.execute("INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, symbol, input_shares, price)

            flash('You have bought!', 'success')
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Main variables
    user_id = session["user_id"]
    info = db.execute("SELECT * FROM history_info WHERE user_id == ?", user_id)
    counter = len(info)

    # If there is not purchase yet it will return nothing
    # Main code is inside HTML For loop and if statement
    if not info:
        return render_template("history.html", info = info)
    else:
        for i in range(counter):
            return render_template("history.html", info = info, i = i, counter = counter)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    else:
        # save user input and give's it to the lookup function
        symbol = lookup(request.form.get("symbol"))

        # take price from lookup function
        value = lookup(request.form.get("symbol"))

        if symbol == None:
            return apology("You need to sign correct Symbol")

        # Take symbol's Name from dict
        symbol = symbol["name"]

        # Take Symbol's Price from dict
        value = value["price"]

        return render_template("quoted.html", symbol=symbol, value=value)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    name = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirmation")

    # this will count, if there is excist username
    check_users = db.execute("SELECT COUNT(*) FROM users WHERE username = ?", name)

    # if there is match count_value dict will return 1
    count_value = check_users[0]['COUNT(*)']

    if request.method == "POST":

        # Chek users registration form
        if not name:
            return apology("user’s input is blank")

        elif not password:
            return apology("Password input is blank")

        elif not confirm:
            return apology("Confirm password input is blank")

        elif password != confirm:
            return apology("Passwords do not match")

        elif count_value != 0:
            return apology("Username already exists")


        # ransform password into hash
        hashed_password = generate_password_hash(password, method='pbkdf2')

        # if there is no apology, then this will insert users information into SQL
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", name, hashed_password)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # this will let user know that registration succesfully complete
        flash('You have successfully registered!', 'success')

        # redirects to homepage
        return redirect("/")

    else:

        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "GET":

        user_id = session["user_id"]
        # Insert symbols with DISTINC method inside html section
        # DISTINC avoides repeted symbols it will SELECT's only once
        quotes = db.execute("SELECT DISTINCT symbol FROM info WHERE user_id == ? AND shares > 0", user_id)

        return render_template("sell.html", quotes = quotes)

    else:

        # Main variables
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        input_shares = int(request.form.get("sell-shares"))

        if input_shares <= 0:
            return apology("Number should be greater then zero")

        # This is how we can have acces into symbol
        # 12: means select chars from 12th char
        # :-2 select last two char which is ' } and removes
        symbol = symbol[12:][:-2]
        price = lookup(symbol)["price"]
        cash = db.execute("SELECT cash FROM users WHERE id == ?", user_id)[0]["cash"]

        shares = db.execute("SELECT shares FROM info WHERE user_id ==? AND symbol == ?", user_id, symbol)[0]["shares"]

        if shares < input_shares:
            return apology("You don't have that many quotes")

        shares -= input_shares

        # Main calculation and Update SQL data
        profit = input_shares * price
        profit += cash
        db.execute("UPDATE info SET shares = shares - ?, total = ? * ? WHERE user_id == ? AND symbol == ?", input_shares, shares, price, user_id, symbol)
        db.execute("UPDATE users SET cash == ? WHERE id == ?", profit, user_id)
        db.execute("INSERT INTO history_info (user_id, symbol, shares, price) VALUES (?, ?, -?, ?)", user_id, symbol, input_shares, price)


        flash('Sold!', 'success')

        return redirect("/")