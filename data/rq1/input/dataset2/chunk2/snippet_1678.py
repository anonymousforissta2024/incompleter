#Source: https://stackoverflow.com/questions/67172339/to-be-exact-this-is-the-error-im-seeing-nameerror-name-solution-is-not-defi
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False