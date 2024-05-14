#Source: https://stackoverflow.com/questions/72084680/typeerror-keyword-argument-not-understood-query-shape-with-keras-and-te
# From PB to h5 -- then load from h5

checkpoint_filepath="drive/MyDrive/Tirocinio/ViT/Model/vit_"+ num_dataset

import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from keras.models import load_model


# LOAD THE PB MODEL
New_Model = tf.keras.models.load_model(checkpoint_filepath) # Loading the Tensorflow Saved Model (PB)
#print(New_Model.summary())

# Saving the Model in H5 Format and Loading it (to check if it is same as PB Format)
tf.keras.models.save_model(New_Model, checkpoint_filepath+'/vit_1_model.h5') # Saving the Model in H5 Format

# LOAD h5
loaded_model_from_h5 = load_model(checkpoint_filepath+'/vit_1_model.h5', custom_objects ={'ShiftedPatchTokenization': ShiftedPatchTokenization, 'PatchEncoder':PatchEncoder, 'MultiHeadAttentionLSA':MultiHeadAttentionLSA}) # Loading the H5 Saved Model
print(loaded_model_from_h5.summary())