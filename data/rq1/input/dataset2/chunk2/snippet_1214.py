#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
from comparteme import app 
from comparteme.models.base_model import User


@app.route('/')
@app.route('/index')
def index():
    User.create(username='Alan')
    return 'returning any string'