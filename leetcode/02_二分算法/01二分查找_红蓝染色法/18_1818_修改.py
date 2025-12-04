from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        s = 0
        best_gain = 0
        sorted_nums1 = sorted(nums1)

        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            s += diff
            # 找出nums1中最接近b的数字
            pos = bisect_left(sorted_nums1, b)
            # 试试左边的
            if pos > 0:
                best_gain = max(best_gain, diff - abs(sorted_nums1[pos-1] - b))
            if pos < len(nums1):
                best_gain = max(best_gain, diff - abs(sorted_nums1[pos] - b))
        return (s - best_gain) % MOD