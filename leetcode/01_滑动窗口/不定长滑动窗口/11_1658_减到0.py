from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x # 窗口总和
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        l = 0
        v = 0
        max_len = -1
        
        
        for r in range(len(nums)):
            v += nums[r]
            while v > target and l <= r:
                v -= nums[l]
                l += 1
            if v == target:
                max_len = max(max_len, r - l + 1)
        return -1 if max_len == -1 else len(nums) - max_len
            
        
nums = [3,2,20,1,1,3]
x = 10
s = Solution()
print(s.minOperations(nums, x))