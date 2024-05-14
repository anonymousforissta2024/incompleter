#Source: https://stackoverflow.com/questions/45965493/labelencoder-typeerror
onehot = pd.DataFrame()
encoders = []
for column in df_resolved.loc[:, ((df_resolved.dtypes != np.int64)&(df_resolved.dtypes != np.int32))]:
    enc = preprocessing.LabelEncoder()
    encoders.append(enc)
    onehot[column] = enc.fit_transform(df_resolved[column])