#Source: https://stackoverflow.com/questions/48719937/getting-typeerror-reduction-operation-argmax-not-allowed-for-this-dtype-when
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, \
    roc_auc_score, roc_curve, recall_score, classification_report
import pandas as pd
import numpy as np


def print_kfold_scores(X_training, y_training):
    print('\nKFold\n')

    fold = KFold(len(y_training), 5, shuffle=False)

    c_param_range = [0.01, 0.1, 1, 10, 100]

    results = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
    results['C_parameter'] = c_param_range

    j = 0
    for c_param in c_param_range:
        print('-------------------------------------------')
        print('C parameter: ', c_param)
        print('\n-------------------------------------------')

        recall_accs = []
        for iteration, indices in enumerate(fold, start=1):
            lr = LogisticRegression(C=c_param, penalty='l1')
            lr.fit(X_training.iloc[indices[0], :], y_training.iloc[indices[0], :].values.ravel())

            y_prediction_undersampled = lr.predict(X_training.iloc[indices[1], :].values)
            recall_acc = recall_score(y_training.iloc[indices[1], :].values, y_prediction_undersampled)
            recall_accs.append(recall_acc)
            print('Iteration ', iteration, ': recall score = ', recall_acc)

        results.ix[j, 'Mean recall score'] = np.mean(recall_accs)
        j += 1
        print('\nMean recall score ', np.mean(recall_accs))
        print('\n')

    best_c_param = results.loc[results['Mean recall score'].idxmax()]['C_parameter'] # Error occurs on this line

    print('*****************************************************************')
    print('Best model to choose from cross validation is with C parameter = ', best_c_param)
    print('*****************************************************************')

    return best_c_param