#Source: https://stackoverflow.com/questions/48702694/attributeerror-nonetype-object-has-no-attribute-items-pil-exif
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    i.load()
    info = i._getexif()
    print(info)
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

get_exif(img_path)