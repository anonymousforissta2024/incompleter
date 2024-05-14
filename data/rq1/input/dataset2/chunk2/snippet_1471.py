#Source: https://stackoverflow.com/questions/62783857/pytorch-typeerror-totensor-object-is-not-iterable
from torchvision import datasets
import torch.utils.data
from torch.utils.data import DataLoader
from torchvision import transforms
from dataset2 import CellsDataset
from torchvision import datasets
import torch
import torchvision
import torchvision.transforms as transforms


class ImageFolderWithPaths(datasets.ImageFolder):
    """Custom dataset that includes image file paths. Extends
    torchvision.datasets.ImageFolder
    """

# override the __getitem__ method. this is the method that dataloader calls
def __getitem__(self, index):
    # this is what ImageFolder normally returns 
    original_tuple = super(ImageFolderWithPaths, self).__getitem__(index)
    # the image file path
    path = self.imgs[index][0]
    # make a new tuple that includes original and the path
    tuple_with_path = (original_tuple + (path,))
    return tuple_with_path

# EXAMPLE USAGE:
# instantiate the dataset and dataloader
data_dir = "/Users/nubstech/Documents/GitHub/CellCountingDirectCount/Eddata/"
dataset = ImageFolderWithPaths(data_dir) # our custom dataset
#dataloader = DataLoader(dataset)
transform = transforms.Compose([
    # you can add other transformations in this list
    transforms.ToTensor()
])
dataset = DataLoader(data_dir, transforms.Compose(transforms.ToTensor()))
dataloader = torch.utils.DataLoader(dataset)

# iterate over data
for inputs, labels, paths in dataloader:
    # use the above variables freely
   print(inputs, labels, paths)