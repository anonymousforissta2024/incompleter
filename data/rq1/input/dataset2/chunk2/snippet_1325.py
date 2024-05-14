#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from gevent import monkey
from flask import Flask, render_template, request
from flask_socketio import SocketIO
monkey.patch_all()

from App.views import test
app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(test.app)
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=80)