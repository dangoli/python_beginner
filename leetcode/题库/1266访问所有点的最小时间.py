from typing import List
from itertools import pairwise

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for (x1,y1), (x2, y2) in pairwise(points):
            ans += max(abs(x2 - x1), abs(y2 - y1))
        return ans