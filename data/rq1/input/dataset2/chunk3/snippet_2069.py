#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from flask_restplus import Api
from flask import Blueprint

from controller.essential_controller import api as essential_ns
'''from controller.author_controller import app as authors_ns'''

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='PublicVoice Backend service',
          version='0.0.1',
          description='PublicVoice Backend service'
          )

api.add_namespace(essential_ns, path='/essentials')