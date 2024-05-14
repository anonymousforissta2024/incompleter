#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
model_checkpoint = "SpanBERT/spanbert-base-cased"
tokenizer = BertTokenizer.from_pretrained(model_checkpoint,add_prefix_space=True)