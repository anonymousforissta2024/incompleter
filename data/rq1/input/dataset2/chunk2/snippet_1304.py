#Source: https://stackoverflow.com/questions/66431069/sending-opencv-image-via-flask-socketio-to-client-causes-typeerror-object-of-ty
image = '{}'.format(image64).split(',')[1]

im_bytes = base64.b64decode(image)
im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
frame = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)