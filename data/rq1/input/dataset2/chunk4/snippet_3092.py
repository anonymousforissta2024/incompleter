#Source: https://stackoverflow.com/questions/71359706/flask-login-attributeerror-str-object-has-no-attribute-is-active
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))