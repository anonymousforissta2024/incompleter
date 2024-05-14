#Source: https://stackoverflow.com/questions/53956264/typeerror-while-looping-through-dictionary-key-and-items
BDT_param_grid1 ={"learning_rate": np.arange(0.1,1.0,0.1),
                  "n_estimators": np.arange(1, 1000, 10),
                  "base_estimator__min_samples_split": np.arange(0.1,1.0,0.1),
                  "base_estimator__min_samples_leaf": np.arange(1,60,1),
                  "base_estimator__max_leaf_nodes": np.arange(2,60,1),
                  "base_estimator__min_weight_fraction_leaf": np.arange(0.1, 0.4, 0.1),
                  "base_estimator__max_features": np.arange(0.1,1,0.1),
                  "base_estimator__max_depth": np.arange(1, 28, 1)}

for key,items in dict.items(BDT_param_grid1):
    print(key,items)