from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        # 第一段
        i = 1
        while i < n and nums[i-1] < nums[i]:
            i += 1
        if i == 1: 
            return False
        
        # 第二段
        i0 = i
        while i < n and nums[i - 1] >  nums[i]:
            i += 1
        if i == i0 or i == n:
            return False
        
        # 第三段
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        return i == n