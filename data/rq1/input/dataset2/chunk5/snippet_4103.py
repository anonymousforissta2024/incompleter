#Source: https://stackoverflow.com/questions/55807656/rows-cols-frame-shape-attributeerror-nonetype-object-has-no-attribute
while True:
    _, frame = cap.read()
    # frame = cv2.resize(frame, None, fx=0.8, fy=0.8)
    rows, cols, _ = frame.shape
    keyboard[:] = (26, 26, 26)
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)