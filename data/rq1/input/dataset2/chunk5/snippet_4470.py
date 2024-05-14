#Source: https://stackoverflow.com/questions/61591232/typeerror-unorderable-types-str-float
from sklearn.ensemble import RandomForestClassifier
text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)  
text_classifier.fit(X_train, y_train)