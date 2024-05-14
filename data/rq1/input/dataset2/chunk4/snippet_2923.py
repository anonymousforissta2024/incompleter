#Source: https://stackoverflow.com/questions/74859282/got-typeerror-when-adding-return-indices-true-to-nn-maxpool2d-in-pytorch
encoder = Encoder().to(device)
decoder = Decoder().to(device)
test_img = torch.unsqueeze(train_data[0], dim=0)
print(encoder(test_img))