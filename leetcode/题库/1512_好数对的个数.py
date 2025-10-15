from collections import Counter
from typing import List
import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 组合问题
        count = Counter(nums) #Counter({1: 3, 3: 2, 2: 1})
        res = 0
        for v in count.values():
            if v > 1:
                res += math.comb(v, 2)
        return res

nums = [1,2,3,1,1,3]
s = Solution()

print(s.numIdenticalPairs(nums))