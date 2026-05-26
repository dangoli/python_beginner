from typing import List
from itertools import accumulate
# 前缀和

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i+1] = s[i] + nums[i]
        
        ans = 0
        for i, num in enumerate(nums):
            ans += s[i+1] - s[max(0, i - num)]

        return ans

nums = [2,3,1]
s = Solution()
print(s.subarraySum(nums))