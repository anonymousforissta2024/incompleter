#Source: https://stackoverflow.com/questions/58497957/typeerror-structural-similarity-takes-2-positional-arguments-but-8-were-given
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
(score, diff) = compare_ssim(gray1, gray2, full=True)