#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_data2,
    data_collator=data_collator,
    tokenizer=tokenizer)