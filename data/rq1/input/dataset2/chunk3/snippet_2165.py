#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from flask import request
from flask_restplus import Resource

from service import essential_service
from models.dto import dto as EssentialDto

api = EssentialDto.EssentialDto.api
essential = EssentialDto.EssentialDto.essential

@api.route('/')
class EssentialController(Resource):
    @api.doc('Get all essential services')
    @api.marshal_list_with(essential, envelope='data')
    def get(self):
        """List all essential service"""
        return essential_service.get_all_service()

    @api.response(201, 'essential services successfully created.')
    @api.doc('create a new essential service')
    @api.expect(essential, validate=True)
    def post(self):
        """Creates a Essential service """
        data = request.json
        return essential_service.create_essential_service(data=data)