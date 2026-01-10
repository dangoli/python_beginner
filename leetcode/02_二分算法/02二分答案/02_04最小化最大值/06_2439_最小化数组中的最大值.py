from typing import List
from bisect import bisect_left
from math import ceil
from itertools import accumulate


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                new_num = nums[i] + extra
                extra = max(new_num - limit, 0)
            return nums[0] + extra <= limit
        return bisect_left(range(max(nums)), True, lo = min(nums), key=check)
    

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((s + i) // (i + 1) for i, s in enumerate(accumulate(nums)))