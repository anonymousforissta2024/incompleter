#Source: https://stackoverflow.com/questions/42123029/how-to-fix-typeerror-connect-failed-between-navigationtoolbar2qt-messagestr
import numpy as np
from numpy import nan
import pandas as pd
import matplotlib as mpl
#import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import pylab as pl
from uncertainties import ufloat
from uncertainties.umath import *
from matplotlib.ticker import MaxNLocator
from collections import OrderedDict
import astropy.units as u
from astropy.cosmology import FlatLambdaCDM, z_at_value
from numpy import sqrt, mean, square, std, maximum, minimum
from sklearn.metrics import mean_squared_error
from scipy.stats import poisson, chi2
import math
import sys