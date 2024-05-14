#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
from flask_sqlalchemy import SQLAlchemy

database_url = "mysql+pymysql://root:xxxx@localhost:3306/db1"
dbbind_url = "oracle://dbuser:xxxx@10.0.0.1:1521/db2" 

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_BINDS"] = {
    'oracle': dbbind_url
     }
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)