#Source: https://stackoverflow.com/questions/59443374/attribute-error-device-in-fast-ai-learner
from fastai.vision import *

data = (ImageList.from_df(train_df, path='/working/')
   .split_by_rand_pct(0.2)
   .label_from_df(label_delim=','))

learner = cnn_learner(data, models.resnet18, metrics=[accuracy])