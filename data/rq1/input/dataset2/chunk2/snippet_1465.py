#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
class BatchGenerator():
    def __init__(self, X, batch_size):
        self.X=X
        self.batch_size=batch_size
        
    def __call__(self):
        indices = np.arange(len(self.X)) 
        batch=[]
        while True:
                for i in indices:
                    batch.append(i)
                    if len(batch)==self.batch_size:
                        yield self.X[batch]
                        batch=[]       

data=pd.read_csv('./test_x_data_OOP3.csv', index_col=[0])
data=np.array(data)
data=reshape_for_Lstm(data)  

batch_generator=BatchGenerator(data, 2)   

converter.representative_dataset = batch_generator