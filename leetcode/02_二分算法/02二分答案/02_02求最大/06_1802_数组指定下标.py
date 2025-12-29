from typing import List

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum

        def sum_n(x: int, cnt: int) -> int:
            if x >= cnt:
                return (x + x - cnt + 1) * cnt // 2
            else:
                return (x + 1) * x // 2 + cnt - x
        
        while left <= right: # 开区间出错了，改闭区间
            mid = (left + right) >> 1
            if sum_n(mid - 1, index) + sum_n(mid, n - index) <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
n = 4
index = 2
maxSum = 6
s = Solution()
print(s.maxValue(n, index, maxSum))