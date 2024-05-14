#Source: https://stackoverflow.com/questions/64175246/keras-model-fit-giving-out-typeerror-nonetype-object-is-not-callable
model.fit([images, negatives], positives, epochs=10, batch_size=8, verbose=2)