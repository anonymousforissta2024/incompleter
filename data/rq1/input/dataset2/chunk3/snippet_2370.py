#Source: https://stackoverflow.com/questions/60479597/error-attributeerror-dataframe-object-has-no-attribute-source-or-keyerr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data_with_anomalies.csv')
source = pd.DataFrame(data)
target = data['Anomaly']
source = source.drop(columns = ['Anomaly_Tag'])

model = ExtraTreesClassifier()
model.fit(source, target)
print(model.feature_importances_)

importances = model.feature_importances_

# Below chunk is referred from another question on stackoverflow
# Sort feature importances in descending order
indices = np.argsort(importances)[::-1]