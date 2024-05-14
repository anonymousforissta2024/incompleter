#Source: https://stackoverflow.com/questions/53693999/torch-utils-data-dataloader-outputs-typeerror-module-object-is-not-callable
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optom
from torchvision import datasets, transforms
from torch.autograd import Variable
kwargs={}
train=torch.utils.data.dataloader(datasets.MNIST("mnist",train=True,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307),(0.3081,) )] ) ),batch_size=64, shuffle=True, **kwargs)