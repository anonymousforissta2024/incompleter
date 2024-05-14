#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
train_examples ={'texts':[x[0] for x in train_set],'tag_names':[x[1] for x in train_set]}
train_data = tokenize_and_align_labels(train_examples,label2id)
_=train_data.pop('offset_mapping')