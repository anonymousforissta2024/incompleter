#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint,id2label=id2label,label2id=label2id,ignore_mismatched_sizes=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)