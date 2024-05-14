#Source: https://stackoverflow.com/questions/67278695/typeerror-name-argument-1-must-be-a-unicode-character-not-str-python
import os
import pandas as pd
import numpy as np
import re

crd = os.getcwd()
df_hash = pd.read_csv(crd +"\\hashtag4.csv", encoding="utf-8")

from genderComputer import GenderComputer
gc = GenderComputer()

df_hash['gender'] = gc.resolveGender(df_hash['full_name'], None)