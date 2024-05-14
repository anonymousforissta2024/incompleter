#Source: https://stackoverflow.com/questions/61569935/when-i-run-this-code-i-got-the-errortypeerror-argument-must-be-a-string-or-nu
lbl_enc = preprocessing.LabelEncoder()
y = lbl_enc.fit_transform(data.name_of_the_column.values)