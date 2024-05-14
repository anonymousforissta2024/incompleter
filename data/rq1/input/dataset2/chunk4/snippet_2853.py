#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
args = TrainingArguments(
    "spanbert_",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=2,
    weight_decay=0.01,
    per_device_train_batch_size=2,

)