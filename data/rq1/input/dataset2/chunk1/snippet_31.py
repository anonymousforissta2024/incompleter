#Source: https://stackoverflow.com/questions/54284937/python-typeerror-umat-missing-required-argument-ranges-pos-2
def detect_face(img):   
    imgUMat = cv2.UMat(img)
    gray = cv2.cvtColor(imgUMat, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if (len(faces)==0):
        return None, None
    (x, y, w, h) = faces[0]
    gray = gray.get()
    return gray[y:y+h,x:x+w], faces[0]

def prepare_training_data():
    faces = []
    labels = []
    for img in photo_name_list: #a collection of file locations as strings
        image = cv2.imread(img)
        face, rect = detect_face(image)
        if face is not None:
            faces.append(face)
            labels.append(me)
    return faces, labels

def test_photos():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, labels = prepare_training_data()
    face_recognizer.train(np.array(faces), np.array(labels))
    face, rect = detect_face(test_photo)
    label = face_recognizer.predict(face)
    if label == me:
        print("it's me")
    else:
        print("it's not me")


test_photos()