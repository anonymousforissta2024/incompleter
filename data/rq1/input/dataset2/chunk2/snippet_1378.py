#Source: https://stackoverflow.com/questions/41320337/attributeerror-type-object-minimalfeatureextractionsettings-has-no-attribute
import numpy as np
import pandas as pd

column_names = ['time_series1', 'time_series2','time_series3']
ts = np.random.rand(6,3)


df_to_extract = pd.DataFrame(data=ts, columns = column_names)

df_to_extract['id'] = 1
df_to_extract['time'] = np.arange(1,7)

#print(df_to_extract)

import tsfresh
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
from tsfresh import extract_relevant_features
from tsfresh.feature_extraction import extract_features, MinimalFeatureExtractionSettings
from tsfresh.feature_extraction.settings import *
from tsfresh.feature_extraction.settings import FeatureExtractionSettings
import tsfresh.feature_extraction.settings
from tsfresh import utilities
from tsfresh import feature_extraction


extracted_features = extract_features(df_to_extract, 
                                      column_id="id", 
                                      column_sort="time", 
                                      parallelization= 'per_kind', 
                                      feature_extraction_settings= MinimalFeatureExtractionSettings)