#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
import json
from application import app
from application import mysql
from flask import render_template, request, Response
from application.models import User, Course, Enrollment

@app.route("/user")
def user():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('''SHOW SCHEMAS;''')
    rv = cursor.fetchall()

    User(user_id=1, first_name="John", last_name="Doh", email="jd@domain.com", password="abc123")
    User(user_id=2, first_name="Jane", last_name="Doh", email="jad@domain.com", password="abc123")

    users = User.objects.all()

    return render_template("user.html", users=users)