# 算nums中的三数异或
from typing import List
from itertools import combinations

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = list(set(nums))
        st = {x ^ y for x,y in combinations(nums, 2)} | {0}
        return len({xy ^ z for xy in st for z in nums})

nums = [1, 3]
s = Solution()
print(s.uniqueXorTriplets(nums))