#Source: https://stackoverflow.com/questions/63847023/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-during-svm-trai
recognizer = SVC(C=1.0, kernel="linear", probability=True)
recognizer.fit(data["embeddings"],labels)