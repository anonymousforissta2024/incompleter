#Source: https://stackoverflow.com/questions/58603924/attributeerror-object-has-no-attribute-user-loader
from flask_login import UserMixin, LoginManager
from flaskapp import db, login_manager




@login_manager.user_loader
def get_user(user):
    try:
        return get_id(user)
    except:
        return None


class User(db.Model,UserMixin):
    id          =db.Column(db.Integer, primary_key=True)
    username    =db.Column(db.String(20),unique=True, nullable=False)
    email       =db.Column(db.String(120), unique=True, nullable=False)
    password    =db.Column(db.String(60), nullable=False)
    powerlevel  =db.Column(db.Integer, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return int(self.id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.powerlevel}')"