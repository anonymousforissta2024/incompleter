#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Users import UserResource
from resources.Projects import ProjectResource
from resources.Actions import ActionResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
# Get by id
api.add_resource(ProjectResource, '/projects/<int:project_id>', endpoint = 'get_by_id')