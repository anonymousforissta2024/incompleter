#Source: https://stackoverflow.com/questions/57904984/sqlalchemy-attributeerror-table-object-has-no-attribute-id
class Catalog(db.Model):
    __tablename__ = 'catalog'

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(60), index=True, nullable=False)
    parent_id     = db.Column(db.Integer, db.ForeignKey('catalog.id'), default=None)
    url           = db.Column(db.String())
    created       = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, index=True, onupdate=datetime.now())

    categories = db.relationship('Catalog', remote_side='catalog.id', backref='parent')

class Competitors(db.Model):
    __tablename__ = 'competitors'

    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(40), index=True, nullable=False)
    base_url      = db.Column(db.String())
    cat_url       = db.Column(db.String())
    created       = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, onupdate=datetime.now(), default=datetime.now())

    sells = db.relationship('Competitors_catalog', backref='competitor', cascade="all, delete-orphan", passive_deletes=True, lazy='dynamic')

class CompCatalog(db.Model):
    __tablename__ = 'compcatalog'

    id            = db.Column(db.Integer, primary_key=True)
    out_id        = db.Column(db.Integer)
    name          = db.Column(db.String(60), index=True, nullable=False)
    top_section   = db.Column(db.Integer, default=None)
    comp_id       = db.Column(db.Integer, db.ForeignKey('competitors.id', ondelete="CASCADE"))
    url           = db.Column(db.String())
    created       = db.Column(db.DateTime, default=datetime.now())
    last_modified = db.Column(db.DateTime, index=True, onupdate=datetime.now())