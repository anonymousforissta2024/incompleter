#Source: https://stackoverflow.com/questions/56303572/how-can-i-solve-this-unknown-label-type-error
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

clf =RandomForestClassifier( n_jobs = 2)

rfe = RFE(clf, n_features_to_select=1)
rfe.fit(X_newDoS, Y_DoS)