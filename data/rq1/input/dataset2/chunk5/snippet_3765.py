#Source: https://stackoverflow.com/questions/46170165/attributeerror-cv2-filestorage-object-has-no-attribute-getnode
import cv2

if __name__ == "__main__":
    savePath = "/home/s/Desktop/Imgcov/"
    filename = savePath + "depth.xml"
    fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_READ)
    matrix = fs.getNode("data") 