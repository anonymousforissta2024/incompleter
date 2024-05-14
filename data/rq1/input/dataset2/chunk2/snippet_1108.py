#Source: https://stackoverflow.com/questions/68815246/typeerror-fit-missing-1-required-positional-argument-y
for name, estimator in sklearn.utils.all_estimators(type_filter='regressor'):
    model =  make_pipeline(StandardScaler(), estimator)
    try:
        scores =  cross_validate(model, X, y, scoring='r2')
        print(name, ': ', np.mean(scores['test_score']))
    except:
        print('Does not get printed.')