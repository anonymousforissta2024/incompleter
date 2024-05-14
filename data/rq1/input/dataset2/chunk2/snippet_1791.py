#Source: https://stackoverflow.com/questions/73187115/fit-attributeerror-in-python3-using-imblearn-ensemble-and-balancedrandomfore
from imblearn.ensemble import BalancedRandomForestClassifier

bal_forest = BalancedRandomForestClassifier(n_estimators=100, random_state=1)
bal_forest.fit(X_train, y_train)