#Source: https://stackoverflow.com/questions/55852727/typeerror-when-adding-cuda-device
import torch
from torch import cuda
if cuda.is_available():
    devic=cuda.device(0)
    layer=torch.rand([5,3,2],requires_grad=True)