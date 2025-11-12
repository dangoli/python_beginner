from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 7708s 时间复杂度O(N)
        max_score = 0
        l = 0
        count = {}
        score = 0

        for r, n in enumerate(nums):
            if n in count and count[n] >= l:
                l = count[n] + 1
            count[n] = r
            score = sum(nums[l:r+1])
            max_score = max(max_score, score)
        return max_score
    
nums = [5,2,1,2,5,2,1,2,5]
s = Solution()
print(s.maximumUniqueSubarray(nums))