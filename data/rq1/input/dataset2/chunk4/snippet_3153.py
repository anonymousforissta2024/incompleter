#Source: https://stackoverflow.com/questions/67034884/typeerrorhash-must-be-unicode-or-bytes-not-int
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

class RegisterForm(Form):
    name = StringField("Name Surname",validators=[validators.Length(min=4,max=25)])
    username = StringField("Username",validators=[validators.Length(min=5,max=35)])
    email = StringField("Email Adress",validators=[validators.Email(message = "Please enter a valid email.")])
    password = PasswordField("Password:",validators=[
        validators.DataRequired(message = "Please enter an email."),
        validators.EqualTo(fieldname="confirm",message = "Your password doesn't match")
    ])
    confirm = PasswordField("Verify Password")

class LoginForm(Form):
    username =StringField("Username")
    password =PasswordField("Password")



app = Flask(__name__) #Flask objesi oluşturuyoruz.
app.secret_key= "ybblog"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] =""
app.config["MYSQL_DB"] ="ybblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register",methods =["GET","POST"])    
def register():
    form =RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data 
        username = form.username.data
        email = form.email.data 
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        
        query = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"
        
        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()

        cursor.close()
        
        flash("Login is succesful.","success")

        return redirect(url_for("index"))
    else:
        return render_template("register.html",form = form)

    return render_template("login.html")


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    
    if request.method == "POST" :
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        query = "Select * From users where username = %s"
        result = cursor.execute(query,(username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Login is succesful.","success")
                return redirect(url_for("index"))
            else:
                flash("Wrong password.","danger")
                return redirect(url_for("login"))    

        else:
            flash("There is no such user.","danger")
            return redirect(url_for("login"))


    return render_template("login.html",form=form)    



if __name__ == "__main__":
    app.run(debug=True)