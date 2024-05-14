#Source: https://stackoverflow.com/questions/68776470/typeerror-preprocess-input-got-an-unexpected-keyword-argument-mode
from keras.applications.vgg16 import preprocess_input
X = preprocess_input(X, mode='tf')  