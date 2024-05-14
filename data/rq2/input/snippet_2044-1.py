import pandas as pd
data_dict = {'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male'], 'Age': [20, 21, 19, 18, 25, 26, 32, 41, 20, 19], 'Annual Income(k$)': [10, 20, 30, 10, 25, 60, 70, 15, 21, 22], 'Spending Score': [30, 50, 48, 84, 90, 65, 32, 46, 12, 56]}
data.to_csv('Customers.csv')
print(data)