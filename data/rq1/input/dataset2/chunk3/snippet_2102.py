#Source: https://stackoverflow.com/questions/54983241/gridsearchcv-and-randomizedsearchcv-sklearn-typeerror-call-missing-1-r
X, W = train_test_split(all_data, test_size=0.2, random_state=42)
clf_lof = LocalOutlierFactor(novelty=True, contamination='auto')
lof_param_dist_rand = {'n_neighbors': np.arange(6, 101, 1), 'leaf_size': 
                      np.arange(30, 101, 10)}
lof_param_grid_exhaustive = {'n_neighbors': np.arange(6, 101, 1), 
                           'leaf_size': np.arange(30, 101, 10)}
gridsearch(clf=clf_lof, param_dist_rand=lof_param_dist_rand, 
param_grid_exhaustive=lof_param_grid_exhaustive, X=X)


clf_svm = svm.OneClassSVM()
svm_param_dist_rand = {'nu': np.arange(0, 1.1, 0.01), 'kernel': ['rbf', 
                     'linear','poly','sigmoid'], 'degree': np.arange(0, 7, 
                      1), 'gamma': scipy.stats.expon(scale=.1),}
svm_param_grid_exhaustive = {'nu': np.arange(0, 1.1, 0.01), 'kernel': 
                            ['rbf', 'linear','poly','sigmoid'], 'degree': 
                            np.arange(0, 7, 1), 'gamma': 0.25}
gridsearch(clf=clf_svm, param_dist_rand=svm_param_dist_rand, 
param_grid_exhaustive=svm_param_grid_exhaustive, X=X)