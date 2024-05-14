#Source: https://stackoverflow.com/questions/67420828/pandas-typeerror-when-using-cudf-dataframe-but-not-pandas
import cudf
from cuml.model_selection import train_test_split

dataTest = cudf.read_csv(MY_DATA)

X = dataTest.iloc[:, [1,12]]
y = dataTest.iloc[:,12]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.2, random_state=610)