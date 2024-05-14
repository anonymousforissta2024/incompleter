#Source: https://stackoverflow.com/questions/50102728/tflearns-fit-method-with-numpy-ndarrays-causing-typeerror
import tflearn.datasets.mnist as mnist
x,y,X,Y=mnist.load_data(one_hot=True)
x=x.reshape([-1,28,28,1])
X=X.reshape([-1,28,28,1])
import tflearn


class Neural_Network():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.epochs=60000

    def main(self):
        cnn=tflearn.layers.core.input_data(shape=[None,28,28,1],name="input_layer")
        cnn=tflearn.layers.conv.conv_2d(cnn,32,2, activation="relu")
        cnn=tflearn.layers.conv.max_pool_2d(cnn,2)
        cnn=tflearn.layers.conv.conv_2d(cnn,32,2, activation="relu")
        cnn=tflearn.layers.conv.max_pool_2d(cnn,2)
        cnn=tflearn.layers.core.flatten(cnn)
        cnn=tflearn.layers.core.fully_connected(cnn,1000,activation="relu")        
        cnn=tflearn.layers.core.dropout(cnn,0.85)
        cnn=tflearn.layers.core.fully_connected(cnn,10,activation="softmax")
        cnn=tflearn.layers.estimator.regression(cnn,learning_rate=0.001)
        modell=tflearn.DNN(cnn)
        modell.fit(self.x,self.y)
        modell.save("mnist.modell")


nn=Neural_Network(x,y)    
nn.main()
nn.predict(X[1])
print("Label for prediction:",Y[1])