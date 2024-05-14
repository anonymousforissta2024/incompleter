#Source: https://stackoverflow.com/questions/59729859/python-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index
data_list = glob('dataset\\training\\*\\*.jpg')
def _load_img():

    for v in data_list:
   #     print("Converting " + v + " to NumPy Array ...")       
        data = np.array(Image.open(v))
        data = data.reshape(-1, img_size)

    return data

def _load_label():
    labels = []
    for path in data_list:
        labels.append(get_label_from_path(path))

    return labels