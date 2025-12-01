from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            lo = lower - nums[i]
            up = upper - nums[i]
            # 接下来只在 i + 1到n-1里面找
            left_idx = bisect_left(nums, lo, i+1, n)
            right_idx = bisect_right(nums, up, i+1, n)
            count += right_idx - left_idx
        return count