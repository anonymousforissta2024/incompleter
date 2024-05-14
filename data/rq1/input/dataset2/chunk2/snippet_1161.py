#Source: https://stackoverflow.com/questions/75026218/python-pytest-mock-the-class-method-typeerror-str-object-is-not-callable
from python_tools.pytest_samples.slow import DataSet


def slow_load():
    dataset = DataSet()
    return dataset.load_data()