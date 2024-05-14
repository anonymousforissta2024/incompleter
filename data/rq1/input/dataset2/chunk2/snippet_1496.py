#Source: https://stackoverflow.com/questions/61620754/plt-suptitle-typeerror-can-only-concatenate-tuple-not-str-to-tuple
import numpy as np
import matplotlib.pyplot as plt

dataset = df
dfsize = dataset[df.columns[0]].size
x = []
for i in range(dfsize):
    x.append(i)

dataset.shape
# dataset.dropna(inplace=True)
dataset.columns.values
var = ""
for i in range(dataset.shape[1]):  ## 1 is for column, dataset.shape[1] calculate length of col

    y = dataset[dataset.columns[i]].values
    y = y.astype(float)
    y = y.reshape(-1, 1)
    y.shape
    from sklearn.impute import SimpleImputer

    missingvalues = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0)
    missingvalues = missingvalues.fit(y)
    y = missingvalues.transform(y[:, :])

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    from sklearn.compose import ColumnTransformer

    labelencoder_x = LabelEncoder()
    x = labelencoder_x.fit_transform(x)

    from scipy.interpolate import *

    p1 = np.polyfit(x, y, 1)
    # from matplotlib.pyplot import *
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.figure()
    plt.xticks(x, months, rotation=25,fontsize=8)
    plt.suptitle(dataset.columns[i] + ' (xyz)', fontsize=10)