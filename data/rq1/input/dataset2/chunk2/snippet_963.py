#Source: https://stackoverflow.com/questions/54377670/error-while-defining-my-keras-model-attributeerror-nonetype-object-has-no
import keras
from keras.layers import *
from keras.models import Model
from keras.activations import softmax
import keras.backend as K

query = Input(name='query', shape=(10,))
doc = Input(name='doc', shape=(100,))
embedding = Embedding(1125, 50, trainable=True)
q_embed = embedding(query)
d_embed = embedding(doc)
q_w = Dense(1, use_bias=False)(q_embed)
q_w = Lambda(lambda x: softmax(x, axis=1), output_shape=(10,))(q_w)
q_w_layer = Lambda(lambda x: K.repeat_elements(q_w, rep=50, axis=2))(q_w)
q_embed = Multiply()([q_w_layer, q_embed])
cross = Dot(axes=[2, 2], normalize=False)([q_embed, d_embed])
cross = Permute((2, 1))(cross)
contxt = Conv1D(30, 5, strides=5, activation='relu', name="conv")(cross)
contxt = BatchNormalization()(contxt)
contxt = Dropout(0.2)(contxt)
attention = Dense(1, use_bias=False)(contxt)
attention = Activation('softmax')(attention)
contxt = Multiply()([contxt, attention])
important_context = MaxPooling1D(pool_size=2, strides=2)
contxt = important_context(contxt)
word_level = Permute((2, 1))(cross)

# ############ This is the part that caused the problem

word_level_padd = K.reshape(ZeroPadding1D((0, contxt.shape[2] - word_level.shape[2]))(K.reshape(word_level,
                                (-1, 
                                 word_level.shape[2], 
                                 word_level.shape[1]
                                ))),
                           (-1, word_level.shape[1], contxt.shape[2])
                           ) if word_level.shape[-1] < contxt.shape[-1] else word_level
contxt_padded = K.reshape(ZeroPadding1D((0, word_level.shape[2] -contxt.shape[2]))(K.reshape(contxt,
                            (-1, 
                             contxt.shape[2], 
                             contxt.shape[1]
                           ))), 
                         (-1, contxt.shape[1], word_level.shape[2])
                         ) if contxt.shape[-1] < word_level.shape[-1] else contxt
contxt = Concatenate(axis=1, name="merge_levels")([word_level_padd, contxt_padded])

# This is the part that caused the problem #############

lstm_units = int(contxt.shape[1])
contxt = Bidirectional(LSTM(lstm_units, return_sequences=False))(contxt)
contxt = BatchNormalization()(contxt)
contxt = Dropout(0.2)(contxt)
out_ = Dense(1)(contxt)
model = Model(inputs=[query, doc], outputs=out_)