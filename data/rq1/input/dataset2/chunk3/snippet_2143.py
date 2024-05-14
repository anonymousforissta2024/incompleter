#Source: https://stackoverflow.com/questions/48094827/typeerror-not-supported-between-instances-of-nonetype-and-str-using-pyn
print(type(firstEmail))

test = tagger.get_entities(firstEmail)
person_ents = test['PERSON']
print (type(person_ents))
for i in person_ents:
    print(i)