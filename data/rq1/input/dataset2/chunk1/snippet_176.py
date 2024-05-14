#Source: https://stackoverflow.com/questions/60296710/attributeerror-dataset-object-has-no-attribute-c-fastai
if __name__ == '__main__':
    dataset_train = NumbersDataset(X_train, y_train)
    dataloader_train = DataLoader(dataset_train, batch_size=4, shuffle=True, num_workers=2)

    dataset_valid = NumbersDataset(X_valid, y_valid)
    dataloader_valid = DataLoader(dataset_valid, batch_size=4, shuffle=True, num_workers=2)

    datas = DataBunch(train_dl = dataloader_train, valid_dl = dataloader_valid)
    leaner = unet_learner(data = datas, arch = models.resnet34)