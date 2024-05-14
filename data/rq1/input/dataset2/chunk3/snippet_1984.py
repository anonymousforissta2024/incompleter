#Source: https://stackoverflow.com/questions/44721821/typeerror-a-common-type-cannot-be-infered-from-types-float-string-in-python
import graphlab

import pandas as pd

import numpy as np

import matplotlib.pyplot as pt

from numpy import array

from graphlab import SFrame


user_columns =['No','User id','User Name','Skill','Given Test Name','Given Test ID','Recommend Test','Recommend Test ID','Time Start','Time End','Score','Max Score']

data=pd.read_table('http://tech4partner.com.cp-in-5.webhostbox.net/recommend_test.php', sep='^',header=None,names = user_columns)

df2 = data.ix[2:]

df3=df2.reset_index()

df4=df3.drop('index', axis=1)

df5=df4.drop(df4.index[len(df4)-1])

df5=df5.reset_index(1,[len(df5)-1])

df7 = df5.reset_index()

df8=df7.drop('index', axis=1)

df9=df8.head(len(df8))

df9.index = np.arange(1, len(df9) + 1)

df9=df9.head(50)

df9