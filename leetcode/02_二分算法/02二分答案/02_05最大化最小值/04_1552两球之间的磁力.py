from typing import List
# 类似2517
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def f(force: int) -> bool:
            cnt = 1
            pre = position[0]
            for p in position[1:]:
                if p - pre >= force:
                    cnt += 1
                    pre = p
            return cnt >= m
        
        position.sort()
        left = 0
        right = position[-1]
        while left + 1 < right:
            mid = (left + right) // 2
            if f(mid):
                left = mid
            else:
                right = mid
        
        return left
    
position = [5,4,3,2,1,1000000000]
m = 2
s = Solution()
print(s.maxDistance(position, m))