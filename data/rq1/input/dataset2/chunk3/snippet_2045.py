#Source: https://stackoverflow.com/questions/58213802/how-to-fix-attributeerror-mapper-object-has-no-attribute-persist-selectable
import os
from datetime import datetime
from flask import Flask
from sqlalchemy.orm.mapper import configure_mappers
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'samplesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/blog'

db = SQLAlchemy()
make_searchable(db.metadata)

class PostQuery(BaseQuery, SearchQueryMixin):
    pass

class Post(db.Model):
    query_class = PostQuery
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    search_vector = db.Column(TSVectorType('title', 'content'))
    image_thumb = db.Column(db.String(255), nullable=False, default='default.jpg')
    slug = db.Column(db.Text)
    publish = db.Column(db.Boolean(), nullable=False, server_default='1')
    headline = db.Column(db.Boolean(), nullable=False)
    dibaca = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return "Post('{self.title}', '{self.date_posted}')"

db.configure_mappers() #very important!

print(Post.query.search(u'something').limit(5).all())