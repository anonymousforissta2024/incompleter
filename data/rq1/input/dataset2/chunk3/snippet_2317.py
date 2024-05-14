#Source: https://stackoverflow.com/questions/73629508/keras-model-fit-typeerror-init-missing-1-required-positional-argument
import os
import sys
import math
import scipy as sp
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

def get_dataset():
    
    SHOW_IMAGE = False

    mnist = tf.keras.datasets.mnist     # 28x28 images of hand-written digits 0-9
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()
    
    X_train = tf.keras.utils.normalize(X_train,axis=1)  # Normalize input datasets between 0 and 1, Helps the NN converge.
    X_test = tf.keras.utils.normalize(X_test,axis=1)

    if (SHOW_IMAGE):
        plt.imshow(X_train[0])
        plt.show()
        input()
        plt.imshow(Y_train[0])
        plt.show()
        input()

    return X_train, Y_train, X_test, Y_test

def high_level_neural_net(X_train, Y_train, X_test, Y_test, M, Nnodes1, Nnodes2, inject_layer, af, MAKE_PLOTS):
    
    class InjectInputCallback(tf.keras.callbacks.Callback):

        # Inject input data to layer between residual blocks; I'm unsure if this works yet.

        def __init__(self,train_dataset,layer,logs=None):
            self.first_trainds = train_dataset
            self.inject_layer = layer

        def on_layer_end(self,layer,logs=None):
            model.layers[self.inject_layer].output = model.layers[self.inject_layer].output + self.first_trainds
           
    print('\n')
    
    print('Building Sequential Model ...\n')
   
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(Nnodes2, activation=tf.nn.relu))                                   # Residual block 1 (hidden layers) 
    model.add(Dense(Nnodes2, activation=tf.nn.relu))                                   # ...
    model.add(Dense(10, activation=tf.nn.relu))                                         # Output layer of residual block 1/Input layer of residual block 2
    model.add(Dense(Nnodes2, activation=tf.nn.relu))                                   # Residual block 2 (hidden layers)
    model.add(Dense(Nnodes2, activation=tf.nn.relu))                                   # ...
    model.add(Dense(10, activation=tf.nn.relu))                                 # Output layer of residual block 2/Output of neural net 

    print('Compiling ...\n')
    model.compile(optimizer=Adam(learning_rate=0.001),  # Uses Adam algorithm as loss function optimizer
                 loss='MeanSquaredError',                                  # sets the model to use MSE as loss function during training
                 metrics=['MeanRelativeError'])                            
    
    print('Fitting Sequential Model with (X_train, Y_train) ...\n') 
    
    #tf.print('X_train = ', X_train, 'with shape', tf.shape(X_train), '\n')
    #tf.print('Y_train = ', Y_train, 'with shape', tf.shape(Y_train), '\n')

    model.fit(x=X_train, y=Y_train, epochs=M)
    #callbacks=[InjectInputCallback(X_train,inject_layer)]

    if (MAKE_PLOTS):
        plt.plot(history.history['MeanSquareError'])
        plt.title('Model Training')
        plt.ylabel('Mean Squared Error')
        plt.xlabel('Epoch')
        plt.legend(['X_Train','Y_Train'], loc='upper right')
        plt.show()

    #print('Evaluating Sequential Model with Analytic Solution...')
    #model.evaluate()
    
    #print('Predicting')
    #model.predict()

    model.build(tf.shape(X_train)) 
    tf.print(model.summary())

if (__name__ == "__main__"):
 
    print("\n")

    MAKE_PLOTS = True               # Turns on plots during training and evaluation of neural net

    M = int(sys.argv[1])            # Number of training iterations
   
    Ninputs = 3             # Number of node inputs
    Nnodes1 = 10            # Number of nodes in layers
    Nnodes2 = 30            # Number of nodes in 2nd and 4th layers
    inject_layer = 3        # layer of neural net where we inject input data to output of layer

    X_train, Y_train, X_test, Y_test = get_dataset()
    high_level_neural_net(X_train, Y_train, X_test, Y_test,  M, Nnodes1, Nnodes2, inject_layer, af, MAKE_PLOTS)