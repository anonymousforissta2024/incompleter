#Source: https://stackoverflow.com/questions/59590849/attributeerror-int-object-has-no-attribute-view1
for epoch in range(epochs):
    # Train for one epoch, then validate
    train(train_loader, model, criterion, optimizer, epoch)
    correct=0
    total=0

    with torch.no_grad():
        losses = validate(val_loader, model, criterion, save_images, epoch)
        for data in enumerate(train_loader):
            input_gray, labels = data
            input_gray = input_gray.view(batch_size,1,64,32)
            input_gray = input_gray.float()

        if use_gpu:
            input_gray, labels = input_gray.to.cuda(), labels.to.cuda()

        output_ab = model(input_gray)
        _, predicted = torch.max(output_ab.data,1)
        total+=labels.size()
        correct+=(predicted==labels).sum().item()

    print("Accuracy train %d %%"%(100*correct/total))
    train_acc.append(100*correct/total)    

    # Save checkpoint and replace old best model if current model is better   
    if losses < best_losses:
        best_losses = losses
        torch.save(model.state_dict(), 'checkpoints/model-epoch-{}-losses-{:.3f}.pth'.format(epoch+1,losses))