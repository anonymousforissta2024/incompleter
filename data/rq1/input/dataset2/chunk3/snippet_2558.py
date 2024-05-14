#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
import os
import unittest

from flask_script import Manager


from api import blueprint
from api.database import  db
from api.database.db import Location, Essential

app = db.init_app()
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()