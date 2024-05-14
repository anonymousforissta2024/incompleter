#Source: https://stackoverflow.com/questions/77108546/typeerror-berttokenizer-object-is-not-callable-bert-base-multilingual-cased
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
model = AutoModel.from_pretrained("bert-base-multilingual-cased")

text = 'welcome to Miami'
inputs = tokenizer(text, return_tensors='pt', padding=True)
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :]
embeddings.detach().cpu().numpy()