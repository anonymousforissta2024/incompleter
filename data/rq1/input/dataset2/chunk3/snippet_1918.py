#Source: https://stackoverflow.com/questions/39329074/attributeerror-request-object-has-no-attribute-params
from wsgiref import simple_server
import falcon

class user(object):
    def on_get(self, req, resp):
        print(req.params['name'])

api = application = falcon.API()

usr = user()
api.add_route('/user', usr)

if __name__ == '__main__':
    http = simple_server.make_server('127.0.0.10', 8000, api)
    http.serve_forever()