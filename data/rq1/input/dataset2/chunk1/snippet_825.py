#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
tokenizer = tr.RobertaTokenizer.from_pretrained("/home/pc/unbiased_toxic_roberta")
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512, return_tensors="pt")


class SEDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_data = SEDataset(train_encodings, train_labels)



def compute_metrics(eval_pred):
    
    logits, labels = eval_pred
   

    predictions = np.argmax(logits, axis=-1)
    
    acc = np.sum(predictions == labels) / predictions.shape[0]
    
    return {"accuracy" : acc}