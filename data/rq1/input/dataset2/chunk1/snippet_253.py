#Source: https://stackoverflow.com/questions/48719937/getting-typeerror-reduction-operation-argmax-not-allowed-for-this-dtype-when
import ExploratoryDataAnalysis as eda
import Preprocessing as processor
import Classification as classify
import pandas as pd


data_path = '/Users/username/college/year-4/fyp-credit-card-fraud/data/'

if __name__ == '__main__':
    df = pd.read_csv(data_path + 'creditcard.csv')
    # eda.init(df)
    # eda.check_null_values()
    # eda.view_data()
    # eda.check_target_classes()
    df = processor.noramlize(df)

    X_training, X_testing, y_training, y_testing, X_training_undersampled, X_testing_undersampled, \
    y_training_undersampled, y_testing_undersampled = processor.resample(df)

    best_c_param = classify.print_kfold_scores(X_training_undersampled, y_training_undersampled)