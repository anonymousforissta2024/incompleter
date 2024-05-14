#Source: https://stackoverflow.com/questions/52008881/flask-attributeerror-blueprint-object-has-no-attribute-response-class
from flask import Flask

...
app = Flask(__name__)

...
...

from my_app.auth.views import bp
app.register_blueprint(bp)