#Source: https://stackoverflow.com/questions/66194956/typeerror-contact-got-an-unexpected-keyword-argument-name-while-using-flask
class contact(db.Model):
    name = db.Column(db.String(120), nullable=False) 
    email = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=True)
    id = db.Column(db.Integer, primary_key=True)