#Source: https://stackoverflow.com/questions/67647299/attributeerror-module-torch-has-no-attribute-rfft-with-pytorch
from skimage import io
import torch
import piq

@torch.no_grad()
def main():
    x = torch.tensor(io.imread('scikit_image\cover\cover_1.tiff')).permute(2, 0, 1)[None, ...] / 255.
    y = torch.tensor(io.imread('scikit_image\stego\stego_1.tiff')).permute(2, 0, 1)[None, ...] / 255.

    fsim_index: torch.Tensor = piq.fsim(x, y, data_range=1., reduction='none')

    print(fsim_index)

if __name__ == "__main__":
    main()