#Source: https://stackoverflow.com/questions/57788626/typeerror-object-of-type-type-has-no-len-linear-search-on-python
def linearSearch(list, targetValue):
    for i in range(0, len(list)):
        if list[i] == targetValue:
            return i #function stops

    return -1

# MAIN

myList = [3, 2, 8, 1, 10]

location = linearSearch(list, 3)
print(location)