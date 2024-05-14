#Source: https://stackoverflow.com/questions/53298661/attributeerror-numpy-ndarray-object-has-no-attribute-as-matrix
for pred in predicted_values:
        mean_squared_errors.append(mean_squared_error(test[output].as_matrix(), \
         pred.as_matrix()))
        r2_scores.append(r2_score(test[output].as_matrix(), pred.as_matrix()))