from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
                right = mid
            else:
                left = mid
        return right