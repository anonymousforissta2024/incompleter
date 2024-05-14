#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
model.fit_generator(
    generator = train_generator,
    #validation_data=val_generator,
    epochs = epochs, 
    steps_per_epoch = 17, 
    callbacks = [csvlogger, reduce_lr, model_checkpoint], 
    max_queue_size = 48,
    workers = cpu_count() - 2,
    use_multiprocessing = True,
)

print(model.evaluate_generator(generator = test_generator))