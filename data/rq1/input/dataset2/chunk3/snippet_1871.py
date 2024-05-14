#Source: https://stackoverflow.com/questions/77577205/getting-attributeerror-when-running-optuna-study
study = optuna.create_study(direction='minimize', sampler=optuna.samplers.GridSampler(search_space))
study.optimize(objective, n_trials=20)