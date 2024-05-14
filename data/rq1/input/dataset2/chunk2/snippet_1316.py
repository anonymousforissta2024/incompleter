#Source: https://stackoverflow.com/questions/55315275/why-am-i-getting-typeerror-image-data-cannot-be-converted-to-float
import tensorflow as tf
import matplotlib.pyplot as plt

def load_and_preprocess_jpeg(imagepath):
    img = tf.read_file(imagepath)
    img_tensor = tf.image.decode_jpeg(img)
    img_tensor.set_shape([792,1224,1])
    img_tensor = tf.reshape(img_tensor, [792,1224])
    img_tensor = tf.cast(img_tensor, tf.float32, name='ImageCast')
    #img_tensor /= 255.0 #Tried with and without
    return img_tensor

def read_data(all_filenames):
    path_Dataset = tf.data.Dataset.from_tensor_slices(all_filenames)
    image_Dataset = path_Dataset.map(load_and_preprocess_jpeg)
    plt.figure(figsize=(8,8))
    temp_DS = image_Dataset.take(4)
    itera = temp_DS.make_one_shot_iterator()
    for n in range(4):
        image = itera.get_next()
        plt.subplot(2,2,n+1)
        plt.imshow(image)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])