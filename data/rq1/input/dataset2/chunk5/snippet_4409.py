#Source: https://stackoverflow.com/questions/53995606/typeerror-tuple-object-does-not-support-item-assignment-on-non-tuple-object
myresults=[('Raven', '18'), ('Cobra', '8'), ('Lion', '6'), ('Otter', '2')]


FirstScore=myresults[0][1]
SecondHighestScore=0
ThirdHighestScore=0
for i in myresults:
    if i[1]==FirstScore:
        FirstPlacePatrols.append(i[0])
for i in myresults:
    print(i[1])
    print(repr(i[1]))
    if int(i[1])<int(FirstScore):
        if int(i[1])>=SecondHighestScore:
            print(i[1])
            i[1]=SecondHighestScore
            SecondPlacePatrols.append(i[0])
for i in myresults:
    if int(i[1])<SecondHighestScore:
        if int(i[1])>=ThirdHighestScore:
            i[0]=ThirdHighestScore
            ThirdPlacePatrols.append(i[0])
print(FirstPlacePatrols)
print(FirstScore)
print(SecondPlacePatrols)
print(SecondHighestScore)
print(ThirdPlacePatrols)
print(ThirdHighestScore)