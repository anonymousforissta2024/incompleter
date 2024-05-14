#Source: https://stackoverflow.com/questions/66364406/attributeerror-smote-object-has-no-attribute-fit-sample
from imblearn.over_sampling import SMOTE
smt = SMOTE(random_state=0)
X_train_SMOTE, y_train_SMOTE = smt.fit_sample(X_train, y_train)