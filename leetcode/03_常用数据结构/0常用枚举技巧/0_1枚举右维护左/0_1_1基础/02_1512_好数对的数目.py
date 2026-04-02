from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        idx = defaultdict(int) # 创建一个空的哈希表
        ans = 0
        for j,x in enumerate(nums):
            if x in idx:
                ans += idx[x]
            idx[x] += 1
        return ans

nums = [1,2,3,1,1,3]
s = Solution()
print(s.numIdenticalPairs(nums))