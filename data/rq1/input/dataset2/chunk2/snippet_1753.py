#Source: https://stackoverflow.com/questions/51126531/resizing-to-bigger-resolution-with-skimage-causes-shape-typeerror-in-keras
for inputs_batch  in train_generator:
    features_batch = vgg_conv.predict(inputs_batch)
    train_features[i * batch_size : (i + 1) * batch_size] = features_batch 
    i += 1
    if i * batch_size >= nImages:
        break