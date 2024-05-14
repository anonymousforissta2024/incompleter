#Source: https://stackoverflow.com/questions/60641448/flask-restful-typeerror-object-of-type-record-is-not-json-serializable
from flask_restful import Resource, Api, reqparse    

class _Weather(Resource):
    #WEATHER
    def get(self):
        #GET WEATHER
        return {'value': Weather.Record}

self.Api.add_resource(_Weather, '/api/weather')