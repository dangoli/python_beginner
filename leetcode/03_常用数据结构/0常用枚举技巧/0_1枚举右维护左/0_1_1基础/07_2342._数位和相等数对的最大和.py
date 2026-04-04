from typing import List
from math import inf

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        mx = [-inf] * 82 # 存储和数位和s对应的nums[i]
        for num in nums:
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            ans = max(ans, mx[s] + num)
            mx[s] = max(mx[s], num)
        return ans