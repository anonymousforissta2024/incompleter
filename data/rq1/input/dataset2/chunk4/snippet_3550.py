#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
class MyDataset(torch.utils.data.Dataset):
    def __init__(self, examples):
        self.encodings = examples
        self.labels = examples['labels']

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        item["labels"] = torch.tensor([self.labels[idx]])
        return item

    def __len__(self):

        return len(self.labels)

train_data=MyDataset(train_data)