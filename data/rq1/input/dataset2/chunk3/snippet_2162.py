#Source: https://stackoverflow.com/questions/57487356/why-does-functools-cmp-to-key-give-me-a-type-error-on-comparison
from typing import List
import functools

def comparison(a: str, b: str):
  print((a, b))
  if len(a) == 0:
    return b
  elif len(b) == 0:
    return a
  elif a[0] < b[0]:
    return a
  elif a[0] > b[0]:
    return b
  else:
    return comparison(a[1:], b[1:])

class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    cmp = functools.cmp_to_key(comparison)
    res = sorted([str(x) for x in nums], key=cmp, reverse=True)
    return ''.join(res)

sol = Solution()
assert '232302' == sol.largestNumber([230, 23, 2])