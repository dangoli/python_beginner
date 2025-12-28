from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2 + 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if all(nums[i] * 2 <= nums[i - mid] for i in range(mid)):
                left = mid
            else:
                right = mid
        return left * 2