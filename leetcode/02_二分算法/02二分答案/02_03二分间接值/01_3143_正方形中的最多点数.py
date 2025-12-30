from typing import List
from bisect import bisect_left

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ans = 0
        def check(size: int) -> bool:
            vis = set()
            for (x,y), c in zip(points, s):
                if abs(x) <= size and abs(y) <= size: # 点在正方形里
                    if c in vis:
                        return True
                    vis.add(c)
            nonlocal ans
            ans = len(vis)
            return False
        bisect_left(range(1_000_000_001), True, key = check)
        return ans