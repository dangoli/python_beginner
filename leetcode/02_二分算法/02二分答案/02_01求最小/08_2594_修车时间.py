from typing import List
from math import isqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars
        while left + 1 < right:
            mid = (left + right) >> 1
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                right = mid
            else:
                left = mid
        return right

ranks = [4,2,3,1]
cars = 10
s = Solution()
print(s.repairCars(ranks,cars))