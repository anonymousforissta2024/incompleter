#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://0.0.0.0:9999')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
while True:
   frame = footage_socket.recv_string()
   img = base64.b64decode(frame)
   print(img)