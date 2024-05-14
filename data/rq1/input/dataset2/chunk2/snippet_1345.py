#Source: https://stackoverflow.com/questions/62343793/attributeerror-classificadorfinal-object-has-no-attribute-log-softmax-when
import torch.nn as nn
from skorch import NeuralNetClassifier #integracao com sklearn
from sklearn.model_selection import cross_val_score,GridSearchCV
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import torch
import torch.nn.functional as F
from torch import nn,optim

class classificadorFinal(nn.Module):
    def __init__(self, activation=F.tanh, neurons=16, initializer=torch.nn.init.uniform_, dropout=0.3):
        ##from melhores_parametros
        super().__init__()
        self.dense0 = nn.Linear(4, neurons)
        initializer(self.dense0.weight)
        self.activation0 = activation
        self.dense1 = nn.Linear(neurons, neurons)
        initializer(self.dense1.weight)
        self.activation1 = activation
        self.dense2 = nn.Linear(neurons, 3)

        self.dropout = nn.Dropout(dropout)

    def forward(self, X):
        X = self.dense0(X)
        X = self.activation0(X)
        X = self.dropout(X)
        X = self.dense1(X)
        X = self.activation1(X)
        X = self.dropout(X)
        X = self.dense2(X)
        return X


criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(classificador.parameters(), lr = 0.001, weight_decay = 0.0001)


#treino
for epoch in range(200):##from melhores_parametros

    running_loss = 0.
    running_accuracy = 0.

    for data in train_loader:
        inputs, labels = data

        optimizer.zero_grad()        

        outputs = classificadorFinal(inputs)

        loss = criterion(outputs, labels)###erro
        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        ps = F.softmax(outputs)

        top_p, top_class = ps.topk(k = 1, dim = 1)

        equals = top_class == labels.view(*top_class.shape)

        running_accuracy += torch.mean(equals.type(torch.float))

    print('Época {:3d}: perda {:3.5f} - precisão {:3.5f}'.format(epoch + 1, running_loss/len(train_loader), running_accuracy/len(train_loader)))