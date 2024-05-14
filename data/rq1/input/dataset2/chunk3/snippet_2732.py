#Source: https://stackoverflow.com/questions/55814099/flask-sqlalchemy-attributeerror-user-query-attribute-is-none
from catalog import app
from catalog.database import conn

...

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database connection
db_connection = SQLAlchemy(app)

# auto map tables
db_connection.Model = automap_base(db_connection.Model)

# models
class User(db_connection.Model, UserMixin):
    __tablename__ = 'user'

    roles = relationship('Role', secondary='role_user',
                         backref=backref('users', lazy='dynamic', cascade='all'), cascade="all, delete-orphan",
                         passive_deletes=True, single_parent=True)


class Role(db_connection.Model, RoleMixin):
    __tablename__ = 'role'


class RoleUser(db_connection.Model):
    __tablename__ = 'role_user'

# datastore
db_user = SQLAlchemyUserDatastore(db_connection, User, Role)

security = Security(app, db_user)

...

# try to look for users by username and password

user = db_user.find_user(username=username, password=password)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = User.query.filter_by(username=username, password=password).all()
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = User.query.filter(username=username, password=password).all()
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter'`