from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(d: int) -> int:
            cnt = 1
            pre = price[0]
            for p in price:
                if p - pre >= d:
                    cnt += 1
                    pre = p
            return cnt
        
        price.sort()
        left = 0
        right = (price[-1] - price[0]) // (k - 1) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if f(mid) >= k: #甜蜜度还能加
                left = mid
            else:
                right = mid
        return left