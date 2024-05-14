#Source: https://stackoverflow.com/questions/64714925/retrieving-typeerror-nonetype-object-is-not-callable-socket
footage_socket = context.socket( zmq.SUB )
footage_socket.bind('tcp://0.0.0.0:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
PUB_TARGET = 'tcp://192.168.56.103:9999'
while True:    
   frame  = footage_socket.recv_string()                         
   source = cv2.imdecode( np.fromstring( base64.b64decode( frame ), dtype = np.uint8),1 )
   frame  = cv2.resize( source,
                     (224,224)
                     ).astype( "float32" )
   image = img_to_array( source )
   image = image.reshape( ( 1,image.shape[0],image.shape[1], image.shape[2]))
   preds = model.predict( preprocess_input( image ) )
   ## connecting to server #######
   context1=zmq.Context()                          
   footage_socket = context1.socket( zmq.PUB )      
   footage_socket.connect( PUB_TARGET )            
   footage_socket.send(preds)
     