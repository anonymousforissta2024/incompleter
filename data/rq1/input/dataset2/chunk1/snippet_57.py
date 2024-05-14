#Source: https://stackoverflow.com/questions/55431356/typeerror-init-got-an-unexpected-keyword-argument-n-folds-sentiment-ana
grid_svm = GridSearchCV(
    pipeline_svm, #object used to fit the data
    param_grid=param_svm, 
    refit=True,  # fit using all data, on the best detected classifier
    n_jobs=-1,  # number of cores to use for parallelization; -1 for "all cores" i.e. to run on all CPUs
    scoring='accuracy',#optimizing parameter
    cv=StratifiedKFold(liked_train,n_folds=5),
)