#Source: https://stackoverflow.com/questions/59613693/attributeerror-mpoimagefile-object-has-no-attribute-shape
images, labels = next(iter(self.loader))
grid = torchvision.utils.make_grid(images)