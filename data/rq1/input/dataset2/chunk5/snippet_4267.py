#Source: https://stackoverflow.com/questions/57833141/filenotfounderror-errno-2-no-such-file-or-directory-even-i-have-image-in-th
# Setting up the image pool
image_path = "C:\\Users\\New\\Desktop\\images"
imgs = os.listdir(image_path)
img_x = img_y = 50 # image size is constant
n_samples = np.size(imgs)
n_samples # 20778 originally

# Loading all images...
images = np.array([np.array(Image.open(image_path +  
imgs).convert("RGB")).flatten() for imgs in os.listdir(image_path)], 
order='F', dtype='uint8')
np.shape(images)