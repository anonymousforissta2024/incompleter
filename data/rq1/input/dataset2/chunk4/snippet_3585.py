#Source: https://stackoverflow.com/questions/66162440/typeerror-dict-object-is-not-callable-while-loading-and-testing-pytorch-model
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

model = torch.load('Final_model.pth.tar')

normalize = transforms.Normalize(mean=[0.4914, 0.4824, 0.4467],std=[0.2471, 0.2435, 0.2616])
transform = transforms.Compose([transforms.ToTensor(),normalize])
val_set = datasets.CIFAR10('../data', train=False,download=True,transform=transform)

for i in range(48,64):
    plt.subplot(4,4,i+1-48)
    plt.subplots_adjust(hspace=1,wspace=1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(val_set.data[i])
    out = model(transform(val_set.data[i]).view(1,3,32,32))[0].tolist()
    plt.xlabel(class_names[out.index(max(out))])