#Source: https://stackoverflow.com/questions/56090377/typeerror-keyword-argument-not-understood-module-when-loading-keras-sav
model= tf.keras.models.load_model(
"saved_models/",
custom_objects=None,
compile=True)