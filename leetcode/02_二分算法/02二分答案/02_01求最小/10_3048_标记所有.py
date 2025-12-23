from typing import List
from bisect import bisect_left

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        if n > m:
            return -1
        done = [0] * n # 避免
        def check(mx: int) -> bool:
            exam, study = n, 0
            for i in range(mx - 1, -1,-1):
                idx = changeIndices[i] - 1
                if done[idx] != mx:
                    done[idx] = mx
                    exam -= 1
                    study += nums[idx]
                elif study:
                    study -= 1
            return exam == 0 and study == 0
        left = n + sum(nums)
        ans = left + bisect_left(range(left, m + 1), True, key=check)
        return -1 if ans>m else ans