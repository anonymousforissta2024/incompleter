#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
import os
import warnings
from collections import Counter
import tqdm
import random
warnings.filterwarnings('ignore')
os.environ["WANDB_DISABLED"] = "true"
os.environ["TOKENIZERS_PARALLELISM"]= "true"
from torchcrf import CRF
from transformers import BertTokenizerFast as BertTokenizer
from transformers import BertForTokenClassification
import torch.nn as nn
import torch.nn.functional as F
log_soft = F.log_softmax
from transformers import (Trainer,TrainingArguments)
from torch.utils.data import TensorDataset
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
n_gpu = torch.cuda.device_count()
torch.cuda.empty_cache()