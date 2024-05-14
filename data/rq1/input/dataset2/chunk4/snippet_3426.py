#Source: https://stackoverflow.com/questions/76399931/attributeerror-cant-pickle-local-object-flask-init-locals-lambda
import pickle

import ProcessBuilder as pb
import ServiceLogger as sl
import SystemRecovery as sr
from flask import Flask, Response
from waitress import serve
from flask_cors import CORS


class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.logger = sl.ServiceLogger()
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response


class ApiServer:

    def __init__(self):
        self.server = None
        self.debug = sr.Recovery().debug
        self.port = sr.Recovery().api_port
        self.host = '127.0.0.1'
        self.logger = sl.ServiceLogger()
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/api/*": {"origins": "*"}})
        self.register_endpoints()
        self.server = pb.ProcessBuilder().create_process(self.run, [self])

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))

    def register_endpoints(self):
        return None

    def start(self):
        self.server.start()

    def run(self):
        print("heyy")
        #serve(self.app, port=self.port, host=self.host)

    def terminate(self):
        self.server.kill()
        return None


a = ApiServer()
a.start()
print("heyy")
a.terminate()
print("thread killed")