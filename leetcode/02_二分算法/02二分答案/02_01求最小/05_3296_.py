from typing import List
from heapq import heapify, heapreplace

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, t, t) for t in workerTimes]
        heapify(h)
        for _ in range(mountainHeight):
            nxt, delta, base = h[0]
            heapreplace(h, (nxt + delta + base, delta + base, base))
        return nxt
    
mountainHeight = 4
workerTimes = [2,1,1]
s = Solution()
print(s.minNumberOfSeconds(mountainHeight, workerTimes))