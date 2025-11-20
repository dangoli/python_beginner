from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        max_l = 0
        l = 0
        for r, ch in enumerate(nums):
            count[ch] += 1
            while count[ch] > k:
                count[nums[l]] -= 1
                l += 1
            max_l = max(max_l, r - l + 1)
        return max_l

nums = [1,2,3,1,2,3,1,2]
k = 2
s = Solution()
print(s.maxSubarrayLength(nums, k))         