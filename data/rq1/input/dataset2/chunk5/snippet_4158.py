#Source: https://stackoverflow.com/questions/42098053/typeerror-object-takes-no-parameters-in-python-3-x
class Media(Resource):

    def get(self):
        m = Media('id', 'taken_time')
        return jsonify(m)
        #return jsonify({'id': 'something', 'takenTime': 'something else'})

media_api = Blueprint('resources.media', __name__)
api = Api(media_api)
api.add_resource(
    Media,
    '/medias',
    endpoint='medias'
)