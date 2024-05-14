#Source: https://stackoverflow.com/questions/61292051/hyperopt-typeerror-because-of-passing-parameters-to-function
from hyperopt import fmin, hp, tpe
space4mean = ({'model_class': func_model,
             'data': small_df,
             'init_a': [],
             'init_k': {hp.choice('winsize', np.arange(100))},
             'train_a': [],
             'train_k': {},
             'pred_a': [],
             'pred_k': {hp.choice('use_new_points', [True, False])}
              })
best = fmin(
    optifunc,
    space4mean,
    algo=tpe.suggest,
    max_evals=100)