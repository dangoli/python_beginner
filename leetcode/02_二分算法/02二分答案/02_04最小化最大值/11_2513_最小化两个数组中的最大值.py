import math
from math import lcm
from bisect import bisect_left

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l = lcm(divisor1, divisor2)
        def check(x: int) -> bool:
            left1 = max(uniqueCnt1 - x // divisor2 + x // l, 0)
            left2 = max(uniqueCnt2 - x // divisor1 + x // l, 0)
            common = x - x // divisor1 - x // divisor2 + x // l
            return common >= left1 + left2
        return bisect_left(range((uniqueCnt1 + uniqueCnt2) * 2 - 1), True, key=check)