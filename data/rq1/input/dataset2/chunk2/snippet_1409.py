#Source: https://stackoverflow.com/questions/55347192/how-to-fix-this-nameerror-name-clf-is-not-defined
#Feature Selection --> Random Forest
def feature_importance(clf):
    # Relative Importance (Features)
    clf.fit(X_train,y_train)
    # Get Feature Importance from the classifier
    feature_importance = clf.feature_importances_
    # Normalize The Features
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    # Sort Features and Creat Horizontal Bar Plot
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0]) + .5
    pl.figure(figsize=(16, 12))
    pl.barh(pos, feature_importance[sorted_idx], align='center', color='#0033CC')
    pl.yticks(pos, np.asanyarray(df.columns.tolist())[sorted_idx])
    pl.xlabel("Relative Importance")
    pl.title("Variable Importance - Random Forest")
    pl.show()


clf_NB = GaussianNB()
clf_SVC = SVC()
clf_RF = RandomForestClassifier(n_estimators = 100)

algorithms = [clf_NB,clf_SVC,clf_RF]

for model in algorithms:
    print("\n")
    print("==============================")
    print("Model: {}".format(model.__class__.__name__))
    print("==============================")
    print("\n")
    print("**********************************************************")
    print("**Training**")
    print("Data Size:",len(X_train))
    # Fit model to training data
    train_classifier(model, X_train, y_train)

    # Predict on training set and compute F1 score
    predict_labels(model, X_train, y_train)

    #Predict on Testing Data
    print("**********************************************************")
    print("**Testing**")
    print("Data Size:",len(X_test))
    predict_labels(model, X_test, y_test)

    if clf == clf_RF:
        print("\n")
        feature_importance(clf_RF)