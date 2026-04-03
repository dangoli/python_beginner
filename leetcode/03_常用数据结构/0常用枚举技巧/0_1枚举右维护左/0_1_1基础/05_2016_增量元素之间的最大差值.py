from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        mini = nums[0]
        for j in range(1, n):
            mini = min(mini, nums[j-1])
            if mini < nums[j]:
                ans = max(ans, nums[j] - mini)

        return ans
    
nums = [7,1,5,4]
s = Solution()
print(s.maximumDifference(nums))