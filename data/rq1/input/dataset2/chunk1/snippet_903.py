#Source: https://stackoverflow.com/questions/64429461/typeerror-iteration-over-a-0-d-tensor
lr = 0.001

num_epochs = 10

model = LSTMClassifier(embed_size=embed_size, 
                       hidden_size=hidden_size, 
                       vocab_size=vocab_size,
                       num_layers=num_layers,
                       num_classes=train_ds.num_classes, 
                       batch_size=batch_size)

if use_gpu:
    model = model.cuda()

criterion = nn.CrossEntropyLoss()

if use_gpu:
    criterion = criterion.cuda()

    optimizer = optim.Adam(model.parameters(), lr=lr, betas=(0.7, 0.99))
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.975)

hist = train(model, train_dl, valid_dl, criterion, optimizer, scheduler, num_epochs)