from typing import List

class Solution:
    def check(self, weights:List[int], target: int, d: int):
        n = len(weights)
        i = cnt = 1
        total = weights[0]
        while i < n:
            while i<n and total + weights[i] <= target:
                total += weights[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_w, sum_w = max(weights), sum(weights)
        left, right = max(max_w, sum_w//days), sum_w
        while left<right:
            mid = (left+right) >> 1
            if self.check(weights, mid, days):
                right = mid
            else:
                left = mid + 1
        return right