#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from flask import Blueprint, render_template, Flask
from flask_socketio import SocketIO
app = Blueprint('app', __name__)

socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('main.html')


@socketio.on('connect', namespace='/dd')
def ws_conn():
    print("connect")
    socketio.emit('msg', {'count': 1}, namespace='/dd')


@socketio.on('disconnect', namespace="/dd")
def ws_disconn():
    print("disconnect")