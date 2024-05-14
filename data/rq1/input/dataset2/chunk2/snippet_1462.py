#Source: https://stackoverflow.com/questions/59266158/python-opencv-probabilistic-hough-line-transform-typeerror-object-of-type-no
# Perform the probabilistic Hough transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)