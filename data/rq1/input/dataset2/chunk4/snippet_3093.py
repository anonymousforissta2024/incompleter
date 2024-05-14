#Source: https://stackoverflow.com/questions/71126455/tensorflow-attributeerror-type-object-h5py-h5-h5pyconfig-has-no-attribute
from statistics import mode

import cv2

from keras.models import load_model

import numpy as np

import utils

from utils.datasets import get_labels

from utils.inference import detect_faces

from utils.inference import draw_text

from utils.inference import draw_bounding_box

from utils.inference import apply_offsets

from utils.inference import load_detection_model

from utils.preprocessor import preprocess_input