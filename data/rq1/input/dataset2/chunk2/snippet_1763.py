#Source: https://stackoverflow.com/questions/60097310/typeerror-unhashable-type-numpy-ndarray-in-python
with open('SJC324.txt') as f:
    data=[]
    for line in f:
        x,y=(line.strip('\n').split())
        data.append([int(x),int(y)])
    initialisation(data)