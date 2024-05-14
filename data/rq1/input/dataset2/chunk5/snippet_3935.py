#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
## Mysql Model (working)
class CUSTOMERS (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
## Oracle Model (not working)
class ACCOUNT(db.Model):
    __tablename__ = 'ACCOUNT'
    __bind_key__ = 'oracle'
    account_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    account = db.Column(db.String(400), nullable=False)