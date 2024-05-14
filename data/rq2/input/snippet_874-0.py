import random

def bogosort(nums):

    def isSorted(nums):
        if len(nums) < 2:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    while not isSorted(nums):
        random.shuffle(nums)
    return nums
nums = [int(item) for item in num1.split(',')]
print(bogosort(nums))