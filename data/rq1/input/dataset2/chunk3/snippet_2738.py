#Source: https://stackoverflow.com/questions/63841876/typeerror-list-object-is-not-an-iterator-tensorflow-custom-metric-callback
iter_val_data = iter(self.validation_data)
for batch in range(batches):
    xVal, yVal = next(iter_val_data)