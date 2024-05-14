#Source: https://stackoverflow.com/questions/54894588/attributeerror-dataframeiterator-object-has-no-attribute-ndim
import pandas as pd
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

train = pd.read_csv('train_labels.csv')

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (32, 32, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

#add the .tif to the end of the file name
train['id'] = train['id'].astype(str)+'.tif'


classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


from keras.preprocessing.image import ImageDataGenerator 
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255, validation_split = 0.1)

training_set = test_datagen.flow_from_dataframe(dataframe = train, 
                                                directory = './train', 
                                                x_col='id', 
                                                y_col='label',
                                                subset = 'training',
                                                target_size=(32, 32), 
                                                batch_size=32, 
                                                shuffle=True,
                                                class_mode = 'binary')

test_set = test_datagen.flow_from_dataframe(dataframe = train, 
                                                directory = './train', 
                                                x_col='id', 
                                                y_col='label',
                                                subset = 'validation',
                                                target_size=(32, 32), 
                                                batch_size=32, 
                                                shuffle=True,
                                                class_mode = 'binary')




classifier.fit_generator(training_set,
                         steps_per_epoch = 50000,
                         epochs = 25,
                         validation_data=test_set,
                         validation_steps= 10000)

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
fpr_keras, tpr_keras, thresholds_keras = roc_curve(classifier,
        predictions.ravel())

from sklearn.metrics import auc
auc_keras = auc(fpr_keras, tpr_keras)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_keras, tpr_keras, label='Keras (area = {:.3f})'.format(auc_keras))
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc='best')
plt.show()