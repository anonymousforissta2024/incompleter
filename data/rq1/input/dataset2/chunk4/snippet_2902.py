#Source: https://stackoverflow.com/questions/45216000/python-max-function-asks-for-src2-typeerror-required-argument-src2-pos-2-no
if any([img[0:3] == imgs_type for img in os.listdir(imgs_path)]):
        current_imgs = list(filter(lambda x: x[0:3] == imgs_type, os.listdir(imgs_path)))
        name_index = max(list(map(lambda x: int(x[4:-4]), current_imgs)))
        imgs = list(filter(lambda x: x[0:3] != imgs_type, os.listdir(imgs_path)))