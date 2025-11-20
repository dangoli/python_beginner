
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return len(nums) - l
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
s = Solution()
print(s.longestOnes(nums, k))