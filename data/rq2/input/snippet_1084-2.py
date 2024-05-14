from bisect import bisect, bisect_left
from collections import Counter

class Solution:

    def three_Sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if len(nums) < 3:
            return triplets
        num_freq = Counter(nums)
        nums = sorted(num_freq)
        max_num = nums[-1]
        for i, v in enumerate(nums):
            if num_freq[v] >= 2:
                complement = -2 * v
                if complement in num_freq:
                    if complement != v or num_freq[v] >= 3:
                        triplets.append([v] * 2 + [complement])
            if v < 0:
                two_sum = -v
                lb = bisect_left(nums, two_sum - max_num, i + 1)
                ub = bisect(nums, two_sum // 2, lb)
                for u in nums[lb:ub]:
                    complement = two_sum - u
                    if complement in num_freq and u != complement:
                        triplets.append([v, u, complement])
        return triplets
nums = [-20, 0, 20, 40, -20, -40, 80]
s = Solution()
print(result)
nums = [1, 2, 3, 4, 5, -6]
result = s.three_Sum(nums)
print(result)