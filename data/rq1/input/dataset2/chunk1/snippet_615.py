#Source: https://stackoverflow.com/questions/64665776/typeerror-cant-pickle-weakref-objects-when-pickling-a-deep-learning-model
pickle.dump(model,open('modelDL.pkl','wb'))