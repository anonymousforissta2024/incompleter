#Source: https://stackoverflow.com/questions/60120290/building-neural-networks-tensorflow-2-0-model-sub-classing-valueerror-typeer
import tensorflow as tf
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Dense, Input
import pandas as pd
import numpy as np


# Read in data-
data = pd.read_csv("iris.csv")

# Get data types for different attributes-
data.dtypes
'''
sepallength    float64
sepalwidth     float64
petallength    float64
petalwidth     float64
class           object
dtype: object
'''


# Get shape of data-
data.shape
# (150, 5)


# Check for missing values-
data.isnull().values.any()
# False

# Perform label encoding for target variable-

# Initialize a label encoder-
le = LabelEncoder()

# Label encode target attribute-
data['class'] = le.fit_transform(data['class'])

# Get different classes which are label encoded-
le.classes_
# array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)

# Split data into features (X) and target (y)-
X = data.drop('class', axis = 1)
y = data['class']


# Get training & testing sets using features and labels-
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Convert from Pandas to numpy arrays-
X_train = X_train.to_numpy()
X_test = X_test.to_numpy()

y_train = y_train.to_numpy()
y_test = y_test.to_numpy()

print("\nTraining and Testing set dimensions:")
print("X_train.shape = {0}, y_train.shape = {1}".format(X_train.shape, y_train.shape))
print("X_test.shape = {0}, y_test.shape = {1}\n".format(X_test.shape, y_test.shape))
# Training and Testing set dimensions:
# X_train.shape = (105, 4), y_train.shape = (105,)
# X_test.shape = (45, 4), y_test.shape = (45,)



class IrisClassifier(Model):

    def __init__(self):
        super(IrisClassifier, self).__init__()

        '''
        self.layer1 = Dense(
            units = 4, activation = 'relu',
            kernel_initializer = tf.keras.initializers.GlorotNormal()
            )
        '''

        self.input_layer = Input(
            shape = (4,)
            )

        self.layer1 = Dense(
            units = 10, activation = 'relu',
            input_dim = 4,
            kernel_initializer = tf.keras.initializers.GlorotNormal()
            )

        self.layer2 = Dense(
            units = 10, activation = 'relu',
            kernel_initializer = tf.keras.initializers.GlorotNormal()
            )

        self.outputlayer = Dense(
            units = 3, activation = 'softmax'
            )


    def call(self, x):
        x = self.input_layer(x)
        x = self.layer1(x)
        x = self.layer2(x)
        # x = self.layer3(x)

        return self.outputlayer(x)


# Instantiate a model of defined neural network class-
model = IrisClassifier()

# Define EarlyStopping callback-
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

# Compile defined model-
model.compile(
    optimizer=tf.keras.optimizers.Adam(lr = 0.001),
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
     )


# Train model-
history2 = model.fit(
    x = X_train, y = y_train,
    validation_data = [X_test, y_test],
    epochs = 50, batch_size = 16,
    callbacks = [callback]
    )