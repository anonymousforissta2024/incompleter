#Source: https://stackoverflow.com/questions/66191969/typeerror-type-new-argument-2-must-be-tuple-not-str
strs = ["flower","flood","flight"]
print(*strs)
print(type(strs))
print(type(*strs))