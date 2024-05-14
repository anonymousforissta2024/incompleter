#Source: https://stackoverflow.com/questions/63044360/receiving-type-error-when-comparing-two-variables-python-3
import time

list = [1,2,3,4,2323449,1,525]

def Search(arr):
    # sorting
    i = 0
    print(f"Given list: {list}")
    print("Sorting...")
    time.sleep(1.75)
    for i in range(len(list)): 
        if i + 1 >= len(list):
            break
        elif  list[i + 1] < list[i]: 
            list.sort()
            print("List has been sorted ")
            print(f"Sorted list: {list}")
    #---------------------------------------
    # searching
    inputCheck = True
    while inputCheck:
        n = input("Enter a number to find in the list: ")
        try:
            int(n)
            inputCheck = False                                                                                                                                                                                            
        except ValueError or TypeError:
            print("Please enter a number")
            time.sleep(0.6)



    print("Searching...")

    l = 0
    h = len(list) - 1 

    while l <= h:
        mid = (l + h) // 2

        if list[mid] == n:
            pos = mid
            print(f"Found at index {pos}")
            break
        else:
            print(n)
            if list[mid] < n:
                l = mid
            else:
                h = mid
            
Search(list)