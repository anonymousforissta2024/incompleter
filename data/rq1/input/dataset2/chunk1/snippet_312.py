#Source: https://stackoverflow.com/questions/50935506/unable-to-drop-column-object-has-no-attribute-error
df.drop(['sodium'],axis=1) 

df = df.drop(['sodium'],axis=1)

df = df.drop (['sodium'], 1, inplace=True)