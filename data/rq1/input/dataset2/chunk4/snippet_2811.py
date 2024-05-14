#Source: https://stackoverflow.com/questions/63841876/typeerror-list-object-is-not-an-iterator-tensorflow-custom-metric-callback
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import Callback

# Get binary classification dataset
data = load_breast_cancer(as_frame=True)
print(data)
df = data['data']
df['target'] = data['target']

# Train Test split
train, test = train_test_split(data, test_size = 0.10, shuffle=False)

# Define features and labels
x_train = train.iloc[:, :-1]
y_train = train.iloc[:, -1]
x_test = test.iloc[:, :-1]
y_test = test.iloc[:, -1]

# https://github.com/keras-team/keras/issues/10472#issuecomment-472543538
class Metrics(Callback):
    
    def __init__(self, val_data, batch_size=20):
        super().__init__()
        self.validation_data = val_data
        self.batch_size = batch_size
    
    def on_train_begin(self, logs={}):
        # print(self.validation_data)
        self.val_f1s = []
        self.val_recalls = []
        self.val_precisions = []
        
    def on_epoch_end(self, epoch, logs={}):
        batches = len(self.validation_data)
        total = batches * self.batch_size
        
        val_pred = np.zeros((total,1))
        val_true = np.zeros((total))
        
        for batch in range(batches):
            xVal, yVal = next(self.validation_data)
            val_pred[batch * self.batch_size : (batch+1) * self.batch_size] = np.asarray(self.model.predict(xVal)).round()
            val_true[batch * self.batch_size : (batch+1) * self.batch_size] = yVal
            
        val_pred = np.squeeze(val_pred)
        _val_f1 = f1_score(val_true, val_pred)
        _val_precision = precision_score(val_true, val_pred)
        _val_recall = recall_score(val_true, val_pred)
        
        self.val_f1s.append(_val_f1)
        self.val_recalls.append(_val_recall)
        self.val_precisions.append(_val_precision)
        
        return

# Define a function that creates a basic model
def make_deep_learning_classifier():
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=x_train.shape[1], kernel_initializer='normal'))
    model.add(Dense(32, activation='relu', input_dim=x_train.shape[1], kernel_initializer='normal'))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return model

# Get our model
model = make_deep_learning_classifier()
print(model.summary())

# Define some params
batch_size = 32

# Call our custom callback
callback = [Metrics(val_data=[x_test, y_test], batch_size=batch_size)] # < Issue here?

# Start training
model.fit(x_train, y_train, epochs=1000, batch_size=batch_size, verbose=1, callbacks=callback, validation_data=(x_test, y_test))
print(Metrics.val_precisions) # < Issue here?