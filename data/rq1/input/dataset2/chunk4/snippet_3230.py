#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
args = TrainingArguments(
    "xlmroberta-finetuned-ner",
#     evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=2,
    weight_decay=0.01,
    per_device_train_batch_size=4,
    # per_device_eval_batch_size=32
    fp16=True
    # bf16=True #Ampere GPU
)