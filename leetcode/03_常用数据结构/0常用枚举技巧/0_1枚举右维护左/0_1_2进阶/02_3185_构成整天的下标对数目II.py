from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = [0] * 24
        for num in hours:
            ans += cnt[(24 - num % 24) % 24]
            cnt[num % 24] += 1
        return ans