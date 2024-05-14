#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
dataset = pd.read_csv("50_Startups.csv")

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

print(x)
print(y)