#Source: https://stackoverflow.com/questions/65548276/applying-inception-but-get-the-attribute-error
from IPython.display import Image, display
Image('images/07_inception_flowchart.png')
         
# Classes and functions for loading and using the Inception model
import inception
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf

tf.__version__

# Download the Inception model
inception.data_dir = 'inception/'

def maybe_download():
    """
    Download the Inception model from the internet if it does not already
    exist in the data_dir. The file is about 85 MB.
    """

    print("Downloading Inception v3 Model ...")
    download.maybe_download_and_extract(url=data_url, download_dir=data_dir)

inception.maybe_download()