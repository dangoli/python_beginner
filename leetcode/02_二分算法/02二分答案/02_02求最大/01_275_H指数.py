from typing import List
from bisect import bisect_left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n
        while left <= right: # 闭区间
            mid = (left + right) >> 1
            if mid > n - bisect_left(citations, mid):
                right = mid - 1
            else:
                left = mid + 1
        return right

n = [1,2,100]
s = Solution()
print(s.hIndex(n))