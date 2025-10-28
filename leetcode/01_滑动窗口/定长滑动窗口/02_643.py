from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ave  = 0
        l = 0
        r = l + k

        while r <= len(nums):
            ave = max(ave, sum(nums[l:r])/k)
            l += 1
            r += 1
        return ave
    
nums = [5]
k = 1
s = Solution()
print(s.findMaxAverage(nums, k))