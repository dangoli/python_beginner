from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        cnt = [0] * 60
        for num in time:
            ans += cnt[(60 - num % 60) % 60]
            cnt[num % 60] += 1
        return ans
    
time = [60, 60, 60]
s = Solution()
print(s.numPairsDivisibleBy60(time))