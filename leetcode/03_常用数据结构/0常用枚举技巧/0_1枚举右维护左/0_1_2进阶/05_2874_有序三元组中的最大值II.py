# 枚举j
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * (n + 1)
        for i in range(n-1, 1, -1):
            suf_max[i] = max(suf_max[i+1], nums[i])
        
        ans = pre_max = 0
        for j, num in enumerate(nums):
            ans = max(ans, (pre_max - num) * suf_max[j+1])
            pre_max = max(pre_max, num)
        
        return ans
    
nums = [12,6,1,2,7]
s = Solution()
print(s.maximumTripletValue(nums))