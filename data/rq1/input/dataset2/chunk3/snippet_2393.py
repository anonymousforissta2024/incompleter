#Source: https://stackoverflow.com/questions/50349213/attributeerror-str-object-has-no-attribute-ndim-unable-to-use-model-predic
features = {}
for images in os.listdir(args["image"]):
    filename = args["image"] + '/' + images
    image = load_img(filename, target_size = inputShape)
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    image = preprocess(image)
    pred = resnet.predict(image)
    image_id = images.split('.')[0]
    features[image_id] = pred
    print('>{}'.format(images))