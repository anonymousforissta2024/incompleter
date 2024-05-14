#Source: https://stackoverflow.com/questions/59338360/how-do-i-resolve-typeerror-not-supported-between-instances-of-int-and-st
model.compile(loss = 'categorical_crossentropy', optimizer = optim, metrics = ['accuracy'])

model_checkpoint = CustomModelCheckpoint(model, './weights_'+model_name+'/epoch_')    

train_generator = DataLoader_video_train('/train_CS.txt',version, batch_size = batch_size)
test_generator = DataLoader_video_test('/test_CS.txt', version, batch_size = batch_size)