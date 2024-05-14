#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
bert_model = BertForTokenClassification.from_pretrained(
                        model_checkpoint,
                        id2label=id2label,
                        label2id=label2id
)
bert_model.config.output_hidden_states=True