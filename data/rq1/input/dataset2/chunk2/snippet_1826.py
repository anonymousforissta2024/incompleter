#Source: https://stackoverflow.com/questions/55875134/wtf-forms-populate-object-attributeerror-heatingcircuit-object-has-no-attribu
class Heatingcircuit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sensor_ID1 = db.Column(db.String(30))
    sensor_ID2 = db.Column(db.String(30))
    sensor_ID3 = db.Column(db.String(30))
    pin_ID1 = db.Column(db.Integer)
    pin_ID2 = db.Column(db.Integer)
    pin_ID3 = db.Column(db.Integer)
    temp = db.Column(db.Float)
    state = db.Column(db.String(9))
    timer = db.relationship('Timers', backref='time')

    def __repr__(self):
        return '{}'.format(self.id)