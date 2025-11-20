from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = sorted(nums)
        for i in range(len(n)):
            if n[i] == original:
                original = original * 2
        return original
    
nums = [2,7,9]
original = 4
s = Solution()
print(s.findFinalValue(nums, original))