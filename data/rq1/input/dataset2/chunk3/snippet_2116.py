#Source: https://stackoverflow.com/questions/67349684/typeerror-while-joining-a-room-with-flask-socketio-5-0-1
@socketio.on('connect')
def connection():
    @socketio.on('join-room')
    def join_room(data):
        roomId = data['roomId']
        camId = data['camId']
        join_room(roomId)
        emit('cam-connected', {'camId': camId}, broadcast=True)
        @socketio.on('disconnect')
        def on_disconnect():
            leave_room(roomId)
            emit('cam-disconnected', {'camId': camId}, broadcast=True)