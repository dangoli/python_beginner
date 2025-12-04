from typing import List
from bisect import bisect_left, bisect_right

# 超出时间限制
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        s = 0
        set_nums1 = set(nums1)
        best_gain = 0

        for a, b in zip(nums1,nums2):
            diff = abs(a - b)
            s += diff
            if best_gain >= diff:
                continue
            if b in set_nums1:
                best_gain = max(best_gain, diff)
                continue
            left, right = b - 1, b+ 1
            while left not in set_nums1 and right not in set_nums1:
                left -= 1
                right += 1
            best_gain = max(best_gain, abs(diff - (right - b)))
        s -= best_gain
        return s % MOD
    
    