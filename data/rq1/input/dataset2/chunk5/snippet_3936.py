#Source: https://stackoverflow.com/questions/43668452/typeerror-listdir-takes-at-most-1-argument-2-given
mypath2 = os.path.join('c:\\trainstcolor2')
images2 = list()


mypath = os.path.join('c:\\trainst2')
images = list()

for item,item2 in os.listdir(mypath,mypath2):

   image = cv2.imread(os.path.join(mypath, item))
   image2 = cv2.imread(os.path.join(mypath2, item2))

   if image is not None:

       images.append(image)
       images2.append(image2)