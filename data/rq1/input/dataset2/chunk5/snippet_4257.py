#Source: https://stackoverflow.com/questions/54575314/typeerror-sequence-item-0-expected-str-instance-nonetype-found
import numpy as np
from sklearn import preprocessing

input_labels=['red','black','red','green','black','yellow','white']
encoder=preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel Mapping:")
for i,item in enumerate(encoder.classes_):
    print(item, '--->',i)

print("\nLabel Mapping:",''.join(print(item, '--->',i) for i,item in 
enumerate(encoder.classes_)))