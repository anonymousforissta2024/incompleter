#Source: https://stackoverflow.com/questions/57291797/dask-attributeerror-dataframe-object-has-no-attribute-getitem-array
import boto3
import dask.dataframe as dd

def import_df(key):
        s3 = boto3.client('s3')
        df = dd.read_csv('s3://.../' + key ,encoding='latin1')
        return df

key = 'Churn/CLEANED_data/file.csv'
train = import_df(key)