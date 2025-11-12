from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0 # 统计当前子数组中0的数量
        l = 0
        max_l = 0
        for r, num in enumerate(nums):
            if num == 0:
                count += 1
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            max_l = max(max_l, r-l+1-count)
        return max_l

nums = [0,1,1,1,0,1,1,0,1]
solution = Solution()
print(solution.longestSubarray(nums))