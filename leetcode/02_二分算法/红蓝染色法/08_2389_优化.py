# 递推算前缀和，然后用二分查找
# 时间复杂度 O((n + m) log n)

from typing import List
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] #原地求前缀和
        for i, q in enumerate(queries):
            queries[i] = bisect_right(nums, q)
        return queries