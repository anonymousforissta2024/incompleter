#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
model = BERT_CRF(bert_model, num_labels=len(label2id))
model.to(device)