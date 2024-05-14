#Source: https://stackoverflow.com/questions/49240581/sqalchemy-postgres-attributeerror-cant-set-attribute
class User(db.Model, UserMixin):
    """
    A user who has an account on the website.
    """

    __tablename__ = 'user'

    id = db.Column(db.Integer,
                   primary_key=True,
                   nullable=False,
                   unique=True,
                   autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    photo = db.Column(db.String, default="No Picture")
    _password = db.Column(db.Binary(60))