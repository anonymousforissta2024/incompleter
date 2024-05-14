#Source: https://stackoverflow.com/questions/75447248/importing-keras-raises-typeerror
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

# Rest of the code isn't necessary as error is raised above 