#Source: https://stackoverflow.com/questions/49908246/opencv-typeerror-int-object-is-not-iterable
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer/trainningData.yml')
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        cv2.putText(img, str(id), (x, y + h), font, 255, (255, 0, 0))
    cv2.imshow("Face", img)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()