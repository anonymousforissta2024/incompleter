#Source: https://stackoverflow.com/questions/76001766/typeerror-cannot-convert-0-0-to-eagertensor-of-dtype-int64
EPOCHS = 500
VAL_SUBSPLITS = 1
#VALIDATION_STEPS = info.splits['test'].num_examples//BATCH_SIZE//VAL_SUBSPLITS
VALIDATION_STEPS = train_n_sample//BATCH_SIZE//VAL_SUBSPLITS
VALIDATION_STEPS = 10
#VALIDATAION_SPILIT=tf.cast(VALIDATAION_SPILIT, tf.int64)
model_history = model.fit(x=train_imgarray, y=trainmask_imgarray, batch_size=BATCH_SIZE, epochs=EPOCHS,
                          steps_per_epoch=STEPS_PER_EPOCH,
                          validation_split=VALIDATAION_SPILIT)