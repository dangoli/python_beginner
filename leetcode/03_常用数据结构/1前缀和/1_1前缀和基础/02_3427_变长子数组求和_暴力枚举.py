from typing import List
# 暴力枚举 

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans += sum(nums[max(0, i - num):(i + 1)])

        return ans
    
nums = [2,3,1]
s = Solution()
print(s.subarraySum(nums))