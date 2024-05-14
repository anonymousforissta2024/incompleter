#Source: https://stackoverflow.com/questions/50236372/typeerror-expected-binary-or-unicode-string-got-0-0
import os
import tarfile
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from six.moves import urllib
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

HOME_PATH = os.getcwd()

""" load the csv file with the lending data and convert to tensors """


def convert_duration(s):
    try:
        if pd.isnull(s):
            return s
        elif s[0] == '<':
            return 0.0
        elif s[:2] == '10':
            return 10.0
        else:
            return np.float(s[0])
    except TypeError:
        return np.float64(s)


def load_data(file_name):
    csv_path = os.path.join(HOME_PATH, file_name)
    csv_data =  pd.read_csv(csv_path, encoding = "ISO-8859-1", dtype={'desc': np.str, 'verification_status_joint': np.str, 'loan_status': np.str},low_memory=False, na_values=[])
    loans = csv_data.loc[csv_data['loan_status'].isin(['Fully Paid', 'Charged Off'])]  # Sort out only fully Paid (Paid) and Charged Off (Default)
    loans['loan_status'] = loans['loan_status'].apply(lambda s: np.int(s == 'Fully Paid')) # Convert to boolean integer
    # Drop Columns with one distinct data field
    for col in loans.columns:
        if loans[col].nunique() == 1:
            del loans[col]
    for col in loans.columns:
        if (loans[col].notnull().sum() / len(loans.index)) < 0.1 :
            del loans[col]

    # Remove all irrelevant columns & hifg prediction columns based on pure descetion
    loans.drop(labels=['id', 'member_id', 'grade', 'sub_grade', 'last_credit_pull_d', 'emp_title', 'url', 'desc', 'title', 'issue_d', 'earliest_cr_line', 'last_pymnt_d','addr_state'], axis=1, inplace=True)

    # Process the text based variables
    # Term
    loans['term'] = loans['term'].apply(lambda s:np.float(s[1:3]))

    loans['emp_length'] = loans['emp_length'].apply(lambda s: convert_duration(s))

    #change zip code to just the first 3 significant digits
    loans['zip_code'] = loans['zip_code'].apply(lambda s:np.float(s[:3]))
    loans.fillna('',inplace=True)
    loan_data = shuffle(loans)
    X = loan_data.drop(labels=['loan_status'], axis=1)
    Y = loan_data['loan_status']
    ## consider processing tensorflow feature columns here and return as one response and standardise at one
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.fit_transform(X_test)
    return (X_train, Y_train), (X_test, Y_test)



def my_input_fn(features, labels, batch_size , shuffle=True):
    # consider changing categorical columns and all
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(buffer_size=100000).repeat(count=None).batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()

def my_eval_fn(features, labels, batch_size , shuffle=True):
    # consider changing categorical columns and all
    dataset = tf.data.Dataset.from_tensor_slices((features,labels))
    dataset = dataset.batch(batch_size)
    return dataset.make_one_shot_iterator().get_next()



#Start on calls to make data available

(X_train, Y_train), (X_test, Y_test) = load_data("loan_data.csv")
print(dict(X_train))

my_feature_columns = []
numerical_columns = ['loan_amnt',
 'funded_amnt',
 'funded_amnt_inv',
 'int_rate',
 'installment',
 'annual_inc',
 'dti',
 'delinq_2yrs',
 'inq_last_6mths',
 'mths_since_last_delinq',
 'mths_since_last_record',
 'open_acc',
 'pub_rec',
 'revol_bal',
 'revol_util',
 'total_acc',
 'total_pymnt',
 'total_pymnt_inv',
 'total_rec_prncp',
 'total_rec_int',
 'total_rec_late_fee',
 'recoveries',
 'collection_recovery_fee',
 'last_pymnt_amnt',
 'collections_12_mths_ex_med',
 'mths_since_last_major_derog',
 'acc_now_delinq',
 'tot_coll_amt',
 'tot_cur_bal',
 'total_rev_hi_lim']

categorical_columns = ['home_ownership',
 'verification_status',
 'pymnt_plan',
 'purpose',
 'initial_list_status',
 'application_type']

for key in numerical_columns:
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))

for key in categorical_columns:
    my_feature_columns.append(tf.feature_column.categorical_column_with_hash_bucket(key=key, hash_bucket_size = 10))

classifier = tf.estimator.LinearClassifier(
        feature_columns=my_feature_columns
        )

classifier.train(
        input_fn=lambda:my_input_fn(X_train, Y_train, 100),
        steps=100
        )

eval_result = classifier.evaluate(
    input_fn=lambda:my_eval_fn(X_test, Y_test, 100)
    )

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))