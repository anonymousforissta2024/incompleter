#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from gevent import monkey
from flask import Flask, render_template, request
from flask_socketio import SocketIO
monkey.patch_all()


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('main.html')



@socketio.on('connect', namespace='/dd')
def ws_conn():
    socketio.emit('msg', {'count': 1}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    print("Disconnected")



if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=80)