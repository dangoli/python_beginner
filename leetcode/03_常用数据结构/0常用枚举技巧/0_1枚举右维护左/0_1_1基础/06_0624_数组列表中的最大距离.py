from typing import List
from math import inf

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mn, mx = inf,-inf # mn是左边数组第一个数的最小值,mx是左边数组最后一个数的最大只
        for a in arrays:
            ans = max(ans, a[-1] - mn, mx - a[0])
            mn = min(mn, a[0])
            mx = max(mx, a[-1])
        return ans