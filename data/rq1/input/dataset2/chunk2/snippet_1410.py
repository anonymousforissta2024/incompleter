#Source: https://stackoverflow.com/questions/74719326/attributeerror-only-occurs-during-pytest-run-custom-classes-or-functions-expor
import pytest
from fastai.vision.all import *

from project.predict import my_func, prediction


model = load_learner('model_path/', cpu=True)
model.load(fast_ai_params.weights)


def my_test():
    pred = prediction(tile_params, model, full_tile_path)

    assert pred.shape