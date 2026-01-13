from typing import List
from bisect import bisect_left

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # solve()返回最大金额为mx时，最多可以偷多少间房子
        def solve(mx: int) -> int:
            f0 = f1 = 0 # f1表示偷到当前房子，最多可偷的数量，f0表示前一间
            for x in nums:
                if x > mx:  # 当前房子的金额大于最大可偷，不偷了
                    f0 = f1
                else: # 金额小于等于最大可偷，可以偷当前房子
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1
        # return bisect_left(range(max(nums)), k, key=solve)
        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if solve(mid) < k:
                left = mid
            else:
                right = mid
        return right
    
nums = [2,3,5,9]
k = 2
s = Solution()
print(s.minCapability(nums, k))