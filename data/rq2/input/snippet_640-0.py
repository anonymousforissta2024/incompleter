def selection_sort(nums):
    for i, n in enumerate(nums):
        mn = min(range(i, len(nums)), key=nums.__getitem__)
        nums[i], nums[mn] = (nums[mn], n)
    return nums
nums = [int(item) for item in user_input.split(',')]
print(selection_sort(nums))