#Source: https://stackoverflow.com/questions/59156303/attributeerror-numpy-ndarray-object-has-no-attribute-where
for pred in outlier_preds:
    if pred == -1:
        index = where(predictions)