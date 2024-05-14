#Source: https://stackoverflow.com/questions/76026737/attributeerror-str-object-has-no-attribute-decode-when-loading-tensorflow-h
import numpy as np
import cv2
from tensorflow.keras.models import load_model
model = load_model("my_model_new.h5")

while True:
    success, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)

    predictions = model.predict(img)
    classIndex = np.argmax(predictions)

    predictions = model.predict(img)
    probVal= np.amax(predictions)
    if probVal > threshold:
        cv2.putText(imgOriginal, str(getClassName(classIndex))+" "+ str(probVal),(50,50),font,1,(0,0,255),1,cv2.LINE_AA)
        cv2.imshow("Original Image", imgOriginal)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break