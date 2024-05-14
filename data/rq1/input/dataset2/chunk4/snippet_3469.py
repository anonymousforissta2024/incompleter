#Source: https://stackoverflow.com/questions/25845161/ws4py-under-cherrypy-under-wsgi-exception-attributeerror-mod-wsgi-input-obje
import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import EchoWebSocket
import atexit
import logging

# see http://tools.cherrypy.org/wiki/ModWSGI
cherrypy.config.update({'environment': 'embedded'}) 
if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)

class Root(object):
    def index(self): return 'I work!'
    def ws(self): print('THIS IS NEVER PRINTED :(')
    index.exposed=True
    ws.exposed=True

# registering the websocket
conf={'/ws':{'tools.websocket.on': True,'tools.websocket.handler_cls': EchoWebSocket}}
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()  

#show stacktraces in console (for some reason this is not default in cherrypy+WSGI)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
logger.addHandler(stream)

application = cherrypy.Application(Root(), script_name='', config=conf)