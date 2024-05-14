#Source: https://stackoverflow.com/questions/76920172/attributeerror-module-pycaret-has-no-attribute-utils
from pycaret.classification import ClassificationExperiment
s = ClassificationExperiment()
s.setup(data, target = 'Class variable', session_id = 123)