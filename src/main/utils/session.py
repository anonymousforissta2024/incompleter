import uuid
import argparse

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import RobertaTokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

class Session:
    working_dir = str(uuid.uuid4())

    lextp = False
    inctp = False

    model_name = '../../lm/classifier/models/pytorch_model.bin'
    tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-small')
    model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-small')
    model.load_state_dict(torch.load(model_name, map_location='cpu'))