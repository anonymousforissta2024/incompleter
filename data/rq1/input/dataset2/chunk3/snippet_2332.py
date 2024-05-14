#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
class Voterlist(db.Model):
    id = db.Column(db.Integer, primary_key=True, default=get_time)
    description = db.Column(db.String(128))
    vendorquery = db.Column(db.String(128))
    campaign = db.Column(db.String(128))
    s3key = db.Column(db.String(128))
    fname = db.Column(db.String(128))
    ftimestamp = db.Column(db.Integer)
    source = db.Column(db.String(128))
    user = db.Column(db.String(128))
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<List {}: {}>'.format(self.id, self.campaign)