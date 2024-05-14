import pandas as pd
data = pd.DataFrame(data_dict)
data.to_csv('Customers.csv')
print(data)