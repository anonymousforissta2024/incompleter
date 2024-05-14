#Source: https://stackoverflow.com/questions/55584454/how-to-fix-type-error-while-concatenating-two-lists
MyList = list(range(1,51))
sublist1 = MyList[-26:-29:-1]
sublist1 = sublist1.reverse()
sublist2 = MyList[25:27:1]
print(sublist1 + sublist2)