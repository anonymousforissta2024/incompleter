#Source: https://stackoverflow.com/questions/27196715/typeerror-float-argument-must-be-a-string-or-a-number-not-a-list-converting
heartdis = heartdis[5:]

heartdis_flt = []

for item in heartdis:

    heartdis_flt.append(float(item))

print(heartdis_flt)