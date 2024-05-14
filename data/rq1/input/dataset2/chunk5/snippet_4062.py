#Source: https://stackoverflow.com/questions/57847177/attributeerror-numpy-ndarray-object-has-no-attribute-predict
import pickle
model = pickle.load(open('model3.pkl','rb'))
print(model.predict([['Finance and Control'], ['EMEA'], ['Professional Services']]))