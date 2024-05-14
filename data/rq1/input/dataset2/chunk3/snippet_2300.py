#Source: https://stackoverflow.com/questions/58649555/typeerror-cannot-unpack-non-iterrable-nonetype-object-zbar-raspberry-pi
from pyzbar import pyzbar
import argparse
import cv2

#code
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="chemin de l'image")
args = vars(ap.parse_args())

#load l'image
image=cv2.imread(args["image"])

#trouver lesQR/barcode dans l'image puisles decoder
barcodes=pyzbar.decode(image)

#loop barcode
for barcode in barcodes:
    #extraire les box des coins et faire un carre rouge autour du
    #barcode reconnu
    (x,y,w,h)=barcode.rect
    cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255), 2)

    #barcode est un byte donc besoin convertir en string en premier
    barcodeData=barcode.data.decode("utf=8")
    barcodeType=barcode.type

    #dessiner data barcode et ecrire sur image
    text="{}({})".format(barcodeData,barcodeType)
    cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0,0,255),2)

    print("[INFO] {} code, contenu: {}".format(barcodeType,barcodeData))

#montrer output
cv2.imshow("Image",image)
cv2.waitKey(0)