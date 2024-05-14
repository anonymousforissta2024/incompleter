#Source: https://stackoverflow.com/questions/66431069/sending-opencv-image-via-flask-socketio-to-client-causes-typeerror-object-of-ty
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
result, encimg = cv2.imencode('.jpg', updated_frame, encode_param)
socketio.emit('response_back', {'image_data': encimg}, namespace='/test')