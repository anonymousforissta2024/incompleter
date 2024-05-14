#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
training_args = tr.TrainingArguments(
#     report_to = 'wandb',
    output_dir='/home/pc/1_Proj_hate_speech/results_roberta',          # output directory
    overwrite_output_dir = True,
    num_train_epochs=20,              # total number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=32,   # batch size for evaluation
    learning_rate=2e-5,
    warmup_steps=1000,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir='./logs3',            # directory for storing logs
    logging_steps=1000,
    evaluation_strategy="epoch"
    ,save_strategy="epoch"
    ,load_best_model_at_end=True
)


trainer = tr.Trainer(
    model=model,                         # the instantiated 🤗 Transformers model to be trained
    args=training_args,                  # training arguments, defined above
    train_dataset=train_data,         # training dataset
    eval_dataset=val_data,             # evaluation dataset
    compute_metrics=compute_metrics
)