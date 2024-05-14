#Source: https://stackoverflow.com/questions/71044447/attributeerror-keyedvectors-object-has-no-attribute-get-keras-embedding
from gensim.models import KeyedVectors

wv = KeyedVectors.load_word2vec_format("german.model", binary = True)

from keras.models import Sequential

model = Sequential()
model.add(wv.get_keras_embedding())