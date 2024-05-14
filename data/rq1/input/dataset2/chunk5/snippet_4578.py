#Source: https://stackoverflow.com/questions/55063427/flask-blueprint-returns-nameerror-when-trying-to-register-blueprint-on-the-app-i
from app import app

app.secret_key=flask_secret_key

app.run(debug=debug)