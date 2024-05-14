#Source: https://stackoverflow.com/questions/66470880/file-not-found-error-while-downloading-image-files
import time
import pandas as pd
import requests

Final1 = pd.read_excel("Sneakers.xlsx")
Final1.index+=1

a = Final1.index.tolist()
Images = Final1["Images"].tolist()
Name = Final1["Name"].str.lower().tolist()
Brand = Final1["Brand"].str.lower().tolist()

s = requests.Session()

for i,n,b,l in zip(a,Name,Brand,Images):
    r = s.get(l).content
    with open("Images//" + f"{i}-{n}-{b}.jpg","wb") as f:
        f.write(r)