#Source: https://stackoverflow.com/questions/77073167/typeerror-expected-str-bytes-or-os-pathlike-object-not-dataframe-videoclass
from torch.utils.data import DataLoader, Dataset,ConcatDataset,default_collate
from torch.utils.data import DistributedSampler
from pytorchvideo.data import labeled_video_dataset

# Create a training dataset
train_dataset = labeled_video_dataset(
    df,  # Provide the DataFrame directly
    clip_sampler=make_clip_sampler(clipmode, video_duration),
    transform=video_transform,
    decode_audio=False
)

# Create a DataLoader for the training dataset
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    num_workers=0,
    pin_memory=True
)