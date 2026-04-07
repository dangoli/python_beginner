from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = [0] * 10
        for x in nums:
            for y,c in enumerate(cnt):
                if c and gcd(y, x % 10) == 1:
                    ans += c
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return ans

nums = [2,5,1,4]
s = Solution()
print(s.countBeautifulPairs(nums))