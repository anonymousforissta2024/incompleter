#Source: https://stackoverflow.com/questions/56324165/python-error-attributeerror-module-scipy-misc-has-no-attribute-logsumexp
from lifetimes.plotting import *
from lifetimes.utils import *
from lifetimes.estimation import *
data = summary_data_from_transaction_data(df, 'CustomerID','InvoiceDate', monetary_value_col='Sales', observation_period_end='2011-12-9')
print(data.head())