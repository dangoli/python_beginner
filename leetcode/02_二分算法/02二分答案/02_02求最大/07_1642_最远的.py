from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        left = 0
        right = len(heights) - 1
        q_h = []
        for i in range(len(heights) - 1):
            q_h.append(max(0, heights[i + 1] - heights[i]))

        def check(k: int) -> bool:
            sumH = 0 # 需要的砖块和
            q = list()
            for i in range(k):
                deltaH = q_h[i]
                if deltaH > 0:
                    heapq.heappush(q, deltaH)
                    if len(q) > ladders:
                        sumH += heapq.heappop(q)
                    if sumH > bricks:
                        return False
            return True
        
        while left <= right:
            mid = (left + right) >> 1
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
s = Solution()
print(s.furthestBuilding(heights, bricks, ladders))