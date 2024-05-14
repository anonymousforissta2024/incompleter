#Source: https://stackoverflow.com/questions/60191935/typeerror-tuple-object-cannot-be-interpreted-as-an-integer-while-creating-dat
class NumbersDataset(Dataset):
    def __init__(self):
        self.X = list(df['input_img'])
        self.y = list(df['mask_img'])

    def __len__(self):
        return len(self.X), len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


if __name__ == '__main__':
    dataset = NumbersDataset()
    dataloader = DataLoader(dataset, batch_size=50, shuffle=True, num_workers=2)
    # print(len(dataset))
    # plt.imshow(dataset[100])
    # plt.show()
    print(next(iter(dataloader)))