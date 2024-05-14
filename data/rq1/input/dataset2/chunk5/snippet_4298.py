#Source: https://stackoverflow.com/questions/71704542/got-error-as-typeerror-list-object-is-not-callable
for line in sys.stdin:
    myList= list(line.split("|"))
    temp=list(myList(0).split(" "))
    list1=()
    list2=()
    newList=()
    for ele in temp:
        if ele.strip():
            list1.append(ele)
    temp=list(mylist(1).split(" "))
    for ele in temp:
        if ele.strip():
            list2.append(ele.strip())
    count=0
    for count in range (len(list1)):      
        newList.append(int(list1(count))*int(list2(count)))
        count=count+1
    print(newList)