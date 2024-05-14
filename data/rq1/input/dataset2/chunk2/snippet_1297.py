#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
data=pd.read_csv('./test_x_data_OOP3.csv', index_col=[0])
data=np.array(data)
data=reshape_for_Lstm(data)  #a function that just transforms the array