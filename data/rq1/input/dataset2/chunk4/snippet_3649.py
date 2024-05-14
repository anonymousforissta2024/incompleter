#Source: https://stackoverflow.com/questions/39884564/when-using-flask-with-python-3-and-simpleitk-0-10-0-together-i-am-getting-attri
from __future__ import print_function
import SimpleITK
from flask import Flask
import time

app = Flask(__name__)


@app.route('/fuse')
def fuse():
    image = SimpleITK.ReadImage("CT/IMG-0002-000001.dcm")

    mean_image = SimpleITK.BoxMean( image, [3,3,1])

    all_keys = image.GetMetaDataKeys()
    for key in all_keys:
        mean_image.SetMetaData(key, image.GetMetaData(key))
    mean_image.SetMetaData("0008|0008", "DERIVED\SECONDARY")
    modification_time = time.strftime("%H%M%S")
    modification_date = time.strftime("%Y%m%d")
    mean_image.SetMetaData("0008|0031", modification_time)
    mean_image.SetMetaData("0008|0021", modification_date)

    print(mean_image.GetMetaData("0008|0031"))
    return "finish"