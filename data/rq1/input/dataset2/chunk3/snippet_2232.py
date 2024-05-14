#Source: https://stackoverflow.com/questions/45692594/opencv-fisherfacerecognizers-train-function-shows-typeerror-src-is-not-a-num
fishface = cv2.face.createFisherFaceRecognizer()
emotions = ["True", "Glasses"]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cimage = clahe.apply(gray)
    detections = detector(cimage, 1)
    landmarks_vectorised = []
    for k, d in enumerate(detections):  # For all detected face instances individually

        shape = predictor(cimage, d)  # Draw Facial Landmarks with the predictor class
        xlist = []
        ylist = []
        for i in range(1, 68):  # Store X and Y coordinates in two lists
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))

        xmean = np.mean(xlist)  # Get the mean of both axes to determine centre of gravity
        ymean = np.mean(ylist)
        xcentral = [(x - xmean) for x in xlist]  # get distance between each point and the central point in both axes
        ycentral = [(y - ymean) for y in ylist]

        if xlist[26] == xlist[
            29]:  # If x-coordinates of the set are the same, the angle is 0, catch to prevent 'divide by 0' error in function
            anglenose = 0
        else:
            anglenose = int(math.atan((ylist[26] - ylist[29]) / (xlist[26] - xlist[29])) * 180 / math.pi)

        if anglenose < 0:
            anglenose += 90
        else:
            anglenose -= 90

        landmarks_vectorised = []

        if len(detections) < 1:
            landmarks_vectorised = "error"

        for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
            landmarks_vectorised.append(x)
            landmarks_vectorised.append(y)
            meannp = np.asarray((ymean, xmean))
            coornp = np.asarray((z, w))
            dist = np.linalg.norm(coornp - meannp)
            anglerelative = (math.atan((z - ymean) / (w - xmean)) * 180 / math.pi) - anglenose
            landmarks_vectorised.append(dist)
            landmarks_vectorised.append(anglerelative)
    return landmarks_vectorised


def make_sets(labels):
    training_data = []
    training_labels = []
    for label in labels:
        training = glob.glob("data\\%s\\*" % label)
        print(len(training))

        for item in training:
            try:
                image = cv2.imread(item)
            except:
                continue
            print(item)

            landmarks_vectorised = get_landmarks(image)

            if landmarks_vectorised == "error":
                print("error with landmarks")
                pass
            else:
                training_data.append(landmarks_vectorised)
                if str(label) == "True":
                    training_labels.append(2)
                elif str(label) == "Glasses":
                    training_labels.append(1)

    print("sets created")
    return training_data, training_labels

def make_sets(labels):
    training_data = []
    training_labels = []
    for label in labels:
        training = glob.glob("data\\%s\\*" % label)
        print(len(training))

        for item in training:
            try:
                image = cv2.imread(item)
            except:
                continue
            print(item)

            landmarks_vectorised = get_landmarks(image)

            if landmarks_vectorised == "error":
                print("error with landmarks")
                pass
            else:
                training_data.append(landmarks_vectorised)
                if str(label) == "True":
                    training_labels.append(2)
                elif str(label) == "Glasses":
                    training_labels.append(1)

    print("sets created")
    return training_data, training_labels


def run_recognizer(emotions):
    training_data, training_labels = make_sets(emotions)
    print("training fisher face classifier")
    print(type(training_data))
    print(type(training_labels))

    npar_train = np.array(training_data)
    npar_trainlabs = np.array(training_labels)
    fishface.train(np.array(training_data), npar_trainlabs)

def update(emotions):
    run_recognizer(emotions)
    fishface.save("glasses.xml")

update(emotions)