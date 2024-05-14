#Source: https://stackoverflow.com/questions/48971429/python-attribute-error-im-not-sure-what-is-causing-this-is-it-because-my-web-c
import cv2
import numpy as np

cap = cv2.Videocapture(0)
while True:
     ret,frame = cap.read()
     cv2.imshow('frame',frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()