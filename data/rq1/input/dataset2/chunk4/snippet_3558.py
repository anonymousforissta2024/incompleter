#Source: https://stackoverflow.com/questions/75964010/attributeerror-batchdataset-object-has-no-attribute-class-indices
class_indices = {}
for key in train_ds.class_indices.keys():
    class_indices[train_ds.class_indices[key]] = key

print(class_indices)