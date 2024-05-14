#Source: https://stackoverflow.com/questions/60904090/typeerror-float-argument-must-be-a-string-or-a-number-not-module
# load and prepare an image
def load_image_pixels(filename, shape):
    # load the image to get its shape
    Image_file = image.load_img(filename)
    width, height = Image_file.size
    # load the image with the required size
    Image_file = image.load_img(filename, target_size=shape)
    # convert to numpy array
    Image_file = image.img_to_array(image)
    # scale pixel values to [0, 1]
    Image_file = Image_file.astype('float32')
    Image_file /= 255.0
    # add a dimension so that we have one sample
    Image_file = expand_dims(Image_file, 0)
    return Image_file, width, height

# define the expected input shape for the model
input_w, input_h = 416, 416
# define our new photo
filename = 'zebra.jpg'
# load and prepare image
Image_file, width, height = load_image_pixels(filename, (input_w, input_h))