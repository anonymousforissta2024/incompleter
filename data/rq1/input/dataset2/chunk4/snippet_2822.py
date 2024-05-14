#Source: https://stackoverflow.com/questions/58040108/attributeerror-str-object-has-no-attribute-mean-validation-score-in-python
GridMean = [result.mean_validation_score for result in 
gridA.cv_results_]
print(GridMean)
plt.plot(k_values, GridMean)
plt.xlabel('Value of "K" for KNN')
plt.ylabel('CrossValidated Accuracy')