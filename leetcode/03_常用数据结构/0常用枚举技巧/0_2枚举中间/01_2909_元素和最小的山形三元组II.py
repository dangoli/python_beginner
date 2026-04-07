from typing import List
from math import inf

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n # 后缀最小值
        suf[-1] = nums[-1]
        for i in range(n-2, 1, -1):
            suf[i] = min(nums[i], suf[i + 1])
        
        ans = inf
        pre = nums[0]
        for j, num in enumerate(nums):
            if pre < num and num >suf[j + 1]:
                ans = min(ans, pre + num[j] + suf[j + 1])
            pre = min(pre, num)
        return ans if ans < inf else -1