#Source: https://stackoverflow.com/questions/62190286/unable-to-understand-dtype-errors-in-opencv2-python
import numpy as np
import cv2


########################
# function#
########################

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    else:
        return


cv2.namedWindow(winname="output")
cv2.setMouseCallback("output", draw_circle)


##########################
######showing images#####
##########################

img = np.zeros((512, 512, 3), dtype=np.int8) #----------- problem here

while True:
    cv2.imshow("output", img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()