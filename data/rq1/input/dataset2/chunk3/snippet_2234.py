#Source: https://stackoverflow.com/questions/43798326/calculation-using-dictionary-keys-and-typeerror
x = 0

for something in dict:
    if something >= max(dict.keys()) - n:
        x += sum(dict[something]) // len(dict[something])