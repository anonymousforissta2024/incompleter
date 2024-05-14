#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
import datetime
from flask import Flask
from flask import render_template
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form
import mongoengine.base


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'davidystephenson',
    'host': 'ds059908.mongolab.com',
    'username': 'david',
    'password': 'opensecret',
    'port': 59908,
}
database = MongoEngine(app)


class Post(database.Document):
    author = database.StringField(
        default='David Y. Stephenson', max_length=255, required=True
    )
    body = database.StringField(required=True)
    comments = database.ListField(
        database.EmbeddedDocumentField('Comment')
    )
    slug = database.StringField(max_length=255, required=True, unique=True)
    tease = database.StringField(max_length=255, required=True)
    time = database.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    title = database.StringField(max_length=255, required=True, unique=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog/')
def blog():
    posts = Post.objects.all()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<slug>')
def post(slug):
    post = Post.objects.get(slug=slug)
    return render_template('post.html', post=post)


@app.route('/blog/new')
def new():
    app.logger.debug(isinstance(Post, mongoengine.base.BaseDocument))
    app.logger.debug(isinstance(Post, mongoengine.base.DocumentMetaclass))
    form = model_form(Post)
    return render_template('new_blog.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)