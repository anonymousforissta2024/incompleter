#Source: https://stackoverflow.com/questions/59020487/getting-typeerror-trying-to-open-a-file-in-write-mode-with-python
# [omitting some setup]

with open(setFile, 'r') as setFile:
    olddata = setFile.readlines()

newdata = ''

for line in olddata:
    newdata += re.sub(regex, newset, line)

with open(setFile, 'w') as setFile:
    setFile.write(newdata)