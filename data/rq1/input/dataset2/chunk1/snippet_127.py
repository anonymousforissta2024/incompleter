#Source: https://stackoverflow.com/questions/58278247/attributeerror-list-object-has-no-attribute-dim-when-predicting-in-pytorch
# coding: utf-8

# In[5]:


import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as utils
import numpy as np

data_np = np.loadtxt('input_preds.csv', delimiter=',')




train_ds = utils.TensorDataset(torch.tensor(data_np, dtype=torch.float32).view(-1,11))

trainset = torch.utils.data.DataLoader(train_ds, batch_size=1, shuffle=True)



# setting device on GPU if available, else CPU, replace .cuda() with .to(device)
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        #self.bn = nn.BatchNorm2d(11)
        self.fc1 = nn.Linear(11, 22)
        self.fc2 = nn.Linear(22, 44)
        self.fc3 = nn.Linear(44, 22)
        self.fc4 = nn.Linear(22, 11)

    def forward(self, x):
        #x = x.view(-1, 11)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        #return F.log_softmax(x, dim=1)
        return x
model1 = torch.load('./1e-2')
model2 = torch.load('./1e-3')

for data in trainset:   
        X = data  
        X = X

        output = model1(X).to(device)
        print(output)