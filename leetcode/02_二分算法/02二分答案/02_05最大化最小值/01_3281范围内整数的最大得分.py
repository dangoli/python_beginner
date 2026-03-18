from typing import List
from math import inf

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(score: int) -> bool: # 判断score满不满足 两两差至少是score
            x = -inf
            for s in start:
                x = max(x + score, s) # 区间内选的数x必须大于区间左断点
                if x > s + d:
                    return False
            return True
        
        left, right = 0, (start[-1] + d - start[0]) // (len(start) - 1) + 1
        while left + 1 < right: # 开区间
            mid = (left + right) // 2
            if check(mid): # 如果mid做score满足条件，
                left = mid # 就右移左端点
            else:
                right = mid

        return left