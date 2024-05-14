#Source: https://stackoverflow.com/questions/69653835/attribute-error-pickle-load-seldon-deployment
import pickle
import pandas as pd
import dill
from MyPipelines.CustomPipelines import MyEncoder
from MyPipelines.CustomPipelines import *
import MyPipelines.CustomPipelines

class my_prediction:
   
    def __init__(self):

        file_name = 'model.sav'
        with open(file_name, 'rb') as model_file:
                self.model = pickle.load(model_file)

    def predict(self, request):
        data = request.get('ndarray')
        columns = request.get('names')
        X = pd.DataFrame(data, columns = columns)
        predictions = self.model.predict(X)
        return predictions