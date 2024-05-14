#Source: https://stackoverflow.com/questions/43274942/falcon-attributeerror-api-object-has-no-attribute-create
import falcon
from resources.static import StaticResource


api = falcon.API()
api.add_route('/', StaticResource())