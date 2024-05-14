#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_data,
    # eval_dataset=train_data,
    # data_collator=data_collator,
    # compute_metrics=compute_metrics,
    tokenizer=tokenizer)
trainer.train()