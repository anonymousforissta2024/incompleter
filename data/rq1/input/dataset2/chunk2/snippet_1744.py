#Source: https://stackoverflow.com/questions/50628407/why-do-i-get-a-typeerror-when-building-a-dict
y = [k["b"].update({"a": k["a"]}) for k in d]
print(y)