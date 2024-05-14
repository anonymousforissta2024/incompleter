#Source: https://stackoverflow.com/questions/49332661/typeerror-nonetype-selection-sort-on-python
import random

def find_smallest(arr):
    """Return the index of the smallest value in an array"""
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

def selection_sort(arr):
    """sort an array by storing smallest value to new array 1 by 1"""
    new_array = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array


my_array = []
for i in range(0, 11):
    my_array.append(random.randint(1, 101))
    print(my_array[i])

sorted_array = selection_sort(my_array)
for i in range(len(sorted_array)):
    print(sorted_array[i])