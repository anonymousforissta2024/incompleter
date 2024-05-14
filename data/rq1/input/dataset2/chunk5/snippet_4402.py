#Source: https://stackoverflow.com/questions/77291113/keras-model-add-nameerror-name-input-shape-is-not-defined
import random
import pickle

import numpy as np
import pandas as pd
from nltk.tokenize import RegexpTokenizer

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

from tensorflow.keras.layers import InputLayer
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop
import keras


text = "This is an interisting text this is a text and i need to make this text longer otherwise it wont work"

tokenizer = RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(text)    # list of individual word with duplicates
#print(tokens)

unique_tokens = np.unique(tokens)
unique_token_index = {token: idx for idx, token in enumerate(unique_tokens)}   


n_words = 10
input_words = []
next_words = []

for i in range(len(tokens)- n_words):
    input_words.append(tokens[i:i + n_words])  
    next_words.append(tokens[i + n_words])   


X = np.zeros((len(input_words), n_words, len(unique_tokens)), dtype=bool)  
Y = np.zeros((len(next_words),len(unique_tokens)),dtype=bool)



for i, words in enumerate(input_words):
    for j, word in enumerate(words):
        X[i, j, unique_token_index[word]] = 1
        Y[i, unique_token_index[next_words[i]]] = 1



model = Sequential()


model.add(LSTM(128, input_shape(n_words, len(unique_tokens)), return_sequence=True))   