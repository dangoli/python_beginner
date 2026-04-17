# 枚举j 枚举中间

# 枚举j
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        sufMax = [0] * (n + 1)
        for i in range(n-1, 1, -1):
            sufMax[i] = max(sufMax[i+1], nums[i])
        
        ans = preMax = 0
        for j, x in enumerate(nums):
            ans = max(ans, (preMax - x) * sufMax[j+1])
            preMax = max(preMax, nums[j])
        return ans
    
nums = [12, 6, 1, 2, 7]
s = Solution()
print(s.maximumTripletValue(nums))