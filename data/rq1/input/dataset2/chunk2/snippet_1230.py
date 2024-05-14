#Source: https://stackoverflow.com/questions/48459963/nameerror-name-x-is-not-defined-x-declared-in-for-loop
list_keywords=['DROP','CREATE','ALTER','COMMENT']
file=open(filename)
for line in file:
    if any(x in line.upper() for x in list_keywords):
        print (line)