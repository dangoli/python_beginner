from typing import List
from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            if cnt[x] > 1:
                return x
            
nums = [5,1,5,2,5,3,5,4]
s = Solution()
print(s.repeatedNTimes(nums))