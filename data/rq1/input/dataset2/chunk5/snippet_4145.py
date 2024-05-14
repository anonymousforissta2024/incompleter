#Source: https://stackoverflow.com/questions/54042911/attributeerror-when-use-cv-score-in-python
import requests
from datetime import datetime
import calendar
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import seaborn as sns
import reshape
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import datasets
from sklearn import metrics
import csv
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import operator
from scipy.stats import pearsonr

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from operator import itemgetter
from sklearn.model_selection import GridSearchCV
clf = GridSearchCV(RFR, parameters)
clf.fit(mov[num_cat_key_feat],labels)
# Utility function to report best scores
def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
              score.mean_validation_score,
              np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")
report(clf.cv_scores_)