#Source: https://stackoverflow.com/questions/65448638/typeerror-unsupported-operand-types-for-nonetype-and-list
def quicksort(array):
    if len(array) < 2:
        return 
    else:
        pivot = array[0] #Recursive case
        less = [i for i in array[1:] if i <= pivot] 
        greater = [i for i in array[1:] if i > pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))