#Source: https://stackoverflow.com/questions/60360550/sqlalchemy-multiple-nested-queries-with-filters-from-one-table-attributeerror
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vente_no = db.Column(db.String(50))
    lampshade = db.Column(db.String(30))
    brocante = db.Column(db.String(30))
    buyer = db.Column(db.String(255))
    pays = db.Column(db.String(255))
    QT = db.Column(db.Integer)
    prix_de_vente = db.Column(db.Float)
    poste = db.Column(db.Float)
    total = db.Column(db.Float)
    bordeaux = db.Column(db.Integer)
    amazon = db.Column(db.String(255))
    bordeaux_euros = db.Column(db.Float)
    bordeaux_comm = db.Column(db.Float)
    amazon_euros = db.Column(db.Float)
    amazon_comm = db.Column(db.Float)
    PID = db.Column(db.Integer, db.ForeignKey("period.id"))
    date = db.Column(db.Date)
    description = db.Column(String(255))

    P_id = db.relationship("Period")

    def __repr__(self):
        return '{}'.format(self.id)