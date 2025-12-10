from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_t = min(time)
        max_t = max(time)
        n = len(time)
        left = min_t * totalTrips // n - 1
        right = min(max_t * ((totalTrips-1)//n + 1), min_t * totalTrips)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid
        return right
    
time = [1,2,3]
totalTrips = 5
s = Solution()
print(s.minimumTime(time, totalTrips))