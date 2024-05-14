#Source: https://stackoverflow.com/questions/54051501/typeerror-ensemble-object-is-not-callable
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import model_selection

classifier_names = ["logistic regression", "linear SVM", "nearest centroids", "decision tree"]
classifiers = [LogisticRegression, LinearSVC, NearestCentroid, DecisionTreeClassifier]

ensemble1 = VotingClassifier(classifiers)
ensemble2 = BaggingClassifier(classifiers)
ensemble3 = AdaBoostClassifier(classifiers)
ensembles = [ensemble1, ensemble2, ensemble3]
seed = 7  

for ensemble in ensembles:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    for classifier in classifiers:
        model = ensemble(base_estimator=classifier, random_state=seed)
        results = model_selection.cross_val_score(ensemble, X, Y, cv=kfold)
        print(results.mean())    