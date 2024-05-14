import collections

class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :return type: int
        """
        count_ele = collections.Counter(nums)
        return count_ele.most_common()[0][0]
print(result)