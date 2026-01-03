from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(mx: int) -> bool:
            if sum((x + mx - 1)//mx for x in quantities) <= n:
                return True
            else:
                return False

        left = 0
        right = max(quantities)
        while left + 1 < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid
        return right
    
n = 6
quantities = [11, 6]
s = Solution()
print(s.minimizedMaximum(n,quantities))