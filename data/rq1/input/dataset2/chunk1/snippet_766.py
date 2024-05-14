#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
import torch.nn as nn
from transformers import AutoModel

class PosModel(nn.Module):
    def __init__(self):
        super(PosModel, self).__init__()
        
        self.base_model = tr.RobertaForSequenceClassification.from_pretrained('/home/pc/unbiased_toxic_roberta')
        self.dropout = nn.Dropout(0.5)
        self.linear = nn.Linear(768, 2) # output features from bert is 768 and 2 is ur number of labels
        
    def forward(self, input_ids, attn_mask):
        outputs = self.base_model(input_ids, attention_mask=attn_mask)
        # You write you new head here
        outputs = self.dropout(outputs[0])
        outputs = self.linear(outputs)
        
        return outputs

model = PosModel()

print(model)