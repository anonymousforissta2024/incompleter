#Source: https://stackoverflow.com/questions/64833301/typeerror-precision-score-got-an-unexpected-keyword-argument-y-pred
print("accuracy:", metrics.accuracy_score(Y_test, Y_pred = pred))

print("precision:", metrics.precision_score(Y_test, Y_pred = pred))

print("recall:", metrics.precision_score(Y_test, Y_pred = pred))

print(metrics.classification_report(Y_test, Y_pred = pred))