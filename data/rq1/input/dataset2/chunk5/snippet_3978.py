#Source: https://stackoverflow.com/questions/55657849/typeerror-trying-to-split-data-randomly-in-training-and-test-set
import numpy as np

segment_relative_path = ["a", "b", "c", "d", "e", "f"]
idx = np.random.permutation(len(segment_relative_path))
train_data = segment_relative_path[idx[:int(0.7*len(idx))]]