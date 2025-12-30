from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        nums = 0 # 答案，合金数
        mx = min(stock) + budget
        for comp in composition:
            def check(n: int) -> bool:
                money = 0
                for s, base, c in zip(stock, comp, cost):
                    if s < base * n:
                        money += (base * n - s) * c
                        if money > budget:
                            return False
                return True
            left, right = nums, mx + 1
            while left + 1 < right:
                mid = (left + right) >> 1
                if check(mid):
                    left = mid
                else:
                    right = mid
            nums = left
        return nums