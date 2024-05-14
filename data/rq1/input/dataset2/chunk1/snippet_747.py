#Source: https://stackoverflow.com/questions/57277959/typeerror-must-be-real-number-not-list
for i in S:
    nr=[((i[0]*p)+(i[1]*q))/(math.sqrt(i[0]**2+i[1]**2)*math.sqrt(p**2+q**2)) for (p,q) in P]
    print(nr)
    dist=math.acos(nr)