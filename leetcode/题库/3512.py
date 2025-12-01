from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        cha = s - (s // k) * k
        return cha

nums = [3,9,7]
k = 5
s = Solution()
print(s.minOperations(nums, k))