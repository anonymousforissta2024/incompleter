#Source: https://stackoverflow.com/questions/56054091/typeerror-predict-got-an-unexpected-keyword-argument-callbacks
import keras.callbacks
from keras.models import load_model

model = load_model(strPath_model)
tb_test = keras.callbacks.TensorBoard(log_dir=strPath_model_test_logs,histogram_freq=0, write_graph=True, write_images=True)

y_test = model.predict(test_val_X, verbose=1, callbacks=[tb_test])