#Source: https://stackoverflow.com/questions/48843776/logisticregression-typeerror-not-supported-between-instances-of-str-and
df['Class'].replace('benign',2, inplace=True)
df['Class'].replace('malignant',4, inplace=True)
df.replace('?',10**9,inplace=True)
df.isnull().values.any()#this gives false, data has no missing value
X = df.drop(['Class','Code'], 1)
X = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X))
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train.astype(int)
y_train.astype(int)
X_train = np.array(X_train)
y_train = np.array(y_train)