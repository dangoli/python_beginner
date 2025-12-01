from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        while nums[0] <= upper // 2:
            n = nums.pop(0) # 不行，pop弹出首个元素，可能导致nums为空。
            lo = lower - n
            up = upper - n
            count += bisect_right(nums, up) - bisect_left(nums, lo)
        return count


nums = [-1, 0]
s = Solution()
print(s.countFairPairs(nums, 1, 1))