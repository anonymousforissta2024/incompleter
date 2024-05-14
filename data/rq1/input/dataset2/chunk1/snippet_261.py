#Source: https://stackoverflow.com/questions/75939176/default-collate-typeerror-batch-must-contain-tensors-numbers-dicts-or-lists
from pathlib import Path
from typing import List

import torch
from torch.utils.data import Dataset
from torchvision.io import read_image


class ApplicationDataset(Dataset):
    def __init__(self, slide_ids: List[str], tile_filenames: List[Path]):
        self.slide_ids = slide_ids
        self.tile_filenames = tile_filenames

    def __len__(self):
        return len(self.tile_filenames)

    def __getitem__(self, idx):
        image = read_image(str(self.tile_filenames[idx]))
        return {
            'image': image,
            'slide_id': self.slide_ids[idx],
            'filename': self.tile_filenames[idx],
        }

    @staticmethod
    def collate(batch):
        images = [batch_item['image'] for batch_item in batch]

        images = torch.stack(images, dim=0)
        slide_ids = torch.tensor([batch_item['slide_id'] for batch_item in batch])
        filenames = [str(batch_item['filename']) for batch_item in batch]

        return images, slide_ids, filenames