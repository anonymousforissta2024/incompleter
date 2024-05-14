#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
app = Blueprint('app', __name__)

socketio = SocketIO(app)