#Source: https://stackoverflow.com/questions/56865740/hyperparameter-optimization-using-kerasclassifier-randomizedsearchcv-typeerror
def neural_network(num_neurons=64,num_layers=4,input_dim=8,
                   output_dim=2,learning_rate=1.0e-05,act='relu',
                   dropout=0.3):
    model = Sequential()

    model.add(Dense(num_neurons,activation='relu',input_dim=input_dim))

    for i in range(1,num_layers):
        model.add(Dense(num_neurons,activation=act))

    model.add(Dropout(dropout))

    model.add(Dense(output_dim,activation='softmax'))

    adam = optimizers.Adam(lr=learning_rate)

    model.compile(adam,
                  loss='categorical_crossentropy',
                  metrics=['accuracy']
                 )
    return model
create_model = neural_network
model = KerasClassifier(build_fn=create_model,verbose=0)
batch_size = [16,32,64]
epochs = [200,300,500]
num_neurons = [64,128,256]
num_layers= [2,4,6]
learning_rate = [0.001, 0.01, 0.1, 0.2, 0.3]
dropout = [0.1,0.3,0.5]
param_grid = dict(batch_size=batch_size,epochs=epochs,
                      num_neurons=num_neurons,
                      num_layers=num_layers,
                      learning_rate=learning_rate,
                      dropout=dropout
                     )
grid = RandomizedSearchCV(estimator=model,param_distributions=param_grid,cv=3,n_iter=3)
grid_result = grid.fit(x,y,epochs=epochs,batch_size=batch_size)