from typing import List

class Solution:
    def check(self, piles: List[int], mid: int, h: int):
        n = len(piles)
        if sum((x - 1)//mid for x in piles) <= h - n:
            return True
        else:
            return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        # left = max(min(piles), (sum(piles) - 1)//h + 1)， 错了
        right = max(piles)
        while left < right:
            mid = (left + right) >> 1
            if self.check(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return right
    
piles = [30,11,23,4,20]
h = 6
s = Solution()
print(s.minEatingSpeed(piles, h))