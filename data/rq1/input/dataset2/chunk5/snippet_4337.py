#Source: https://stackoverflow.com/questions/72453120/typeerror-unhashable-type-list
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = int(len(nums)/2)
        ind = -1
        
        if(nums[middle] == target):
            return ind
        elif (nums[middle] > target):
            ind = middle
            nums = nums[:middle-1]
            print(nums)
            search(nums, target)
        else:
            ind = middle
            nums = nums[middle:len(nums)-1]
            print(nums)
            search(nums, target)