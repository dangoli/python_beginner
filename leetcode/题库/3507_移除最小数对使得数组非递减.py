from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        def is_no_decreasing(a: List[int]) -> bool:
            for i in range(1, len(a)):
                if a[i] < a[i-1]:
                    return False
            return True
        
        while not is_no_decreasing(nums):
            k = 0
            s = nums[0] + nums[1]
            for i in range(1, len(nums) - 1):
                t = nums[i] + nums[i+1]
                if s > t:
                    s = t
                    k = i
            nums[k] = s
            nums.pop(k + 1)
            ans += 1
        return ans