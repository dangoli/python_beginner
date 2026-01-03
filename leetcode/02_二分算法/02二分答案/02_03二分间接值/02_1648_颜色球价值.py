from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        left, right = 0, max(inventory)
        T = -1
        while left <= right:
            mid = (left + right) >> 1
            total = sum(ai - mid for ai in inventory if ai >= mid)
            if total <= orders:
                T = mid
                right = mid - 1
            else:
                left = mid + 1
        range_sum = lambda x, y: (x + y) * (y - x + 1) // 2
        rest = orders - sum(ai - T for ai in inventory if ai >= T)
        ans = 0
        for ai in inventory:
            if ai >= T:
                if rest > 0:
                    ans += range_sum(T, ai)
                    rest -= 1
                else:
                    ans += range_sum(T + 1, ai)
        return ans % MOD