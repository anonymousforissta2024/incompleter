#Source: https://stackoverflow.com/questions/74611572/bayesianoptimization-search-errors-out-typeerror-float-object-is-not-subscri
# Search hyperparameters

SEED = 121

# NN

tuner_nn = BayesianOptimization(nn_builder,
objective = 'val_loss',
max_trials = 20,
seed = SEED,
directory = '/Users/myuser/Documents/kerastuner',
overwrite = True
)

tuner_nn.search(x_train, y_train, epochs=50, validation_data=(x_val, ), verbose=0, callbacks=[Earlystopping])

## Build model based on the optimized hyperparameters

besthp_nn = tuner_nn.get_best_hyperparameters()[0]
model_nn = tuner_nn.hypermodel.build(besthp_nn)

# lstm

tuner_lstm = BayesianOptimization(lstm_builder,
objective = 'val_loss',
max_trials = 20,
seed = SEED,
directory = '/Users/myuser/Documents/kerastuner')

tuner_lstm.search(x_train, y_train, epochs=50, validation_data=(x_val, y_val), verbose=0, callbacks=[Earlystopping])

## Build model based on the optimized hyperparameters

besthp_lstm = tuner_lstm.get_best_hyperparameters()[0]
model_lstm = tuner_lstm.hypermodel.build(besthp_lstm)

# gru

tuner_gru = BayesianOptimization(gru_builder,
objective = 'val_loss',
max_trials = 20,
seed = SEED,
directory = '/Users/myuser/Documents/kerastuner')

tuner_gru.search(x_train, y_train, epochs=50, validation_data=(x_val, y_val), verbose=0, callbacks=[Earlystopping])

## Build model based on the optimized hyperparameters

besthp_gru = tuner_gru.get_best_hyperparameters()[0]
model_gru = tuner_gru.hypermodel.build(besthp_gru)