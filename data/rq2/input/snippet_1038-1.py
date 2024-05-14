import copy

def remove_list_of_lists(color, N):
    for x in color:
        del x[N]
    return color
nums = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
nums1 = copy.deepcopy(nums)
nums3 = copy.deepcopy(nums)
print('Original list of lists:')
print(nums)
N = 0
print('\nRemove 1st item from the said list of lists:')
print(remove_list_of_lists(nums1, N))
N = 1
print('\nRemove 2nd item from the said list of lists:')
print(remove_list_of_lists(nums2, N))
N = 3
print('\nRemove 4th item from the said list of lists:')
print(remove_list_of_lists(nums3, N))