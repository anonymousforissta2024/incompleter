#Source: https://stackoverflow.com/questions/64895320/attributeerror-shuffledataset-object-has-no-attribute-features
import tensorflow_datasets as tfds
ds, ds_info = tfds.load('eurosat/rgb:2.0.0',
                    with_info=True,
                    split='train',
                    data_dir='../input/eurosat',
                    download=False)
ds = ds.shuffle(1024)
tfds.show_examples(ds, ds_info);