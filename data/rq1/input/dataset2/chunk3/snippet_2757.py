#Source: https://stackoverflow.com/questions/54223591/how-to-prevent-typeerror-list-indices-must-be-integers-or-slices-not-tuple-in
#Array
Days = ["Mon1","Tue1","Wed1","Thu1","Fri1","Mon2","Tue2","Wed2","Thu2","Fri2","Mon3","Tue3","Wed3","Thu3","Fri3","Mon4","Tue4","Wed4","Thu4","Fri4"]
Buses = ["A","B","C","D","E","F"]
BusData = [ [0,0,0,2,2], [4,0,3,4,-2], [-5,0,0,3,4], [-1,8,1,1,-2],  #Bus A
            [0,1,0,0,1], [2,0,0,0,0], [1,0,0,0,2], [0,0,1,0,0],   #Bus B
            [2,0,-1,-1,-2], [-2,-3,-1,0,0], [-2,0,1,1,1], [1,-1,-1,2,-2] #Bus C
            [1,0,0,0,0], [0,0,0,0,0], [2,0,0,0,0], [0,0,0,0,0], #Bus D
            [-1,-1,-1,-2,-4], [-10,-2,0,0,0], [0,1,2,-3,1], [1,3,-1,0,0]  #Bus E
            [0,-5,-5,-5,-4], [-3,-5,0,0,0], [0,-2,-3,1,1], [1,0,0,-2,-5] ] #Bus F

for i in BusData:
    count = 0
    for x in i:
        if x < 0:
            count +=1
    print("Bus {} was late {} times".format(Buses[BusData.index(i)], count))