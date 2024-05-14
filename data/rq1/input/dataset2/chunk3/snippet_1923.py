#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://172.168.1.2:5555')
videoFile = 'data.mp4'
camera = cv2.VideoCapture(videoFile) 
length=int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
while True:        
  grabbed, frame = camera.read()
  try:
   frame = cv2.resize(frame, (224, 224))
  except cv2.error:
    break
  encoded, buffer = cv2.imencode('.jpg', frame)
  jpg_as_text = base64.b64encode(buffer)
  footage_socket.send(jpg_as_text)