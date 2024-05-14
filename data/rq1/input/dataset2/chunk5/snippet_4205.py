#Source: https://stackoverflow.com/questions/53775393/chainer-cnn-typeerror-forward-missing-1-required-positional-argument-x
from chainer.datasets import split_dataset_random
from chainer.iterators import SerialIterator
from chainer.optimizers import Adam
from chainer.training import Trainer
from chainer.training.updaters import StandardUpdater
from chainer import functions as F, links as L
from chainer import Sequential

import numpy as np

batch_size = 3

X_train = np.ones((9957, 60, 80, 3), dtype=np.float32)
X_train, _ = split_dataset_random(X_train, 8000, seed=0)
train_iter = SerialIterator(X_train, batch_size)

model = Sequential(
    L.Convolution2D(None, 64, 3, 2),
    F.relu,
    L.Convolution2D(64, 32, 3, 2),
    F.relu,
    L.Linear(None, 16),
    F.dropout,
    L.Linear(16, 4)
)

model_loss = L.Classifier(model)
optimizer = Adam()
optimizer.setup(model_loss)
updater = StandardUpdater(train_iter, optimizer)
trainer = Trainer(updater, (25, 'epoch'))

trainer.run()