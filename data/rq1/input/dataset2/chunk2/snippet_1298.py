#Source: https://stackoverflow.com/questions/50628407/why-do-i-get-a-typeerror-when-building-a-dict
x = [dict(a=k["a"], **k["b"]) for k in d]
print(x)