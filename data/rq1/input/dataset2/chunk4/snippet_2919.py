#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
class MyDataset(torch.utils.data.Dataset):
    def __init__(self, examples):
        self.encodings = examples
        print(self.encodings)
        print()
        self.labels = examples['labels']

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        print(item)
        item["labels"] = torch.tensor([self.labels[idx]])
        return item

    def __len__(self):

        return len(self.labels)