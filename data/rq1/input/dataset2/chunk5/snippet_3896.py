#Source: https://stackoverflow.com/questions/59711670/tensorflow-backend-error-attributeerror-module-tensorflow-has-no-attribute
import pandas as pd, numpy as np, os, re, json, math, time 
from keras.models import Sequential 
from keras.layers import Dense 
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import KFold 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline 
from sklearn.model_selection import train_test_split 