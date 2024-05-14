#Source: https://stackoverflow.com/questions/63460126/typeerror-type-object-is-not-subscriptable-in-a-function-signature
nums = [4,5,6,7,8,9]
target = 13

def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        answer = []
 
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})

print(twoSum(nums, target))