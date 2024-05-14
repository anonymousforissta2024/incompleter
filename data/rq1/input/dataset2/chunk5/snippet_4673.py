#Source: https://stackoverflow.com/questions/55391144/in-what-way-can-i-debug-this-attribute-error-in-python
import pandas as pd

data = pd.read_csv("China_FDIGDP.csv")

data1 = data.dropna()
data1.to_csv("data1.csv", index = False)

Data  = pd.read_csv("data1.csv")

print(Data)

x = pd.Data["GDP"].values()
y = pd.Data["FDI_net_in"].values()