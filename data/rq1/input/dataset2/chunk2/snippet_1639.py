#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
def batch_generator():
    for X in data:
        batch_size = 2
        indices = np.arange(len(X)) 
        batch=[]
        while True:
                for i in indices:
                    batch.append(i)
                    if len(batch)==batch_size:
                        yield X[batch]
                        batch=[]

data=pd.read_csv('./test_x_data_OOP3.csv', index_col=[0])
data=np.array(data)
data=reshape_for_Lstm(data) 

converter.representative_dataset = batch_generator