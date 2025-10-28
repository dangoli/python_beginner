from typing import List
# 时间复杂度O(nk)
"""
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        s = 0
        for i in range(k-1, len(nums)):
            c = len(set(nums[i-k+1:i+1]))
            if c >= m:
                s = max(s, sum(nums[i-k+1:i+1]))
        return s
"""
# 时间复杂度O(n)
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        only_arr = {}
        temp = 0
        for i in range(k):
            if nums[i] not in only_arr:
                only_arr[nums[i]] = 1
            else:
                only_arr[nums[i]] += 1
            temp += nums[i]
        ret = temp
        if len(only_arr) < m:
            ret = 0
        
        for i in range(k, len(nums)):
            if nums[i] in only_arr:
                only_arr[nums[i]] += 1
            else:
                only_arr[nums[i]] = 1
            if only_arr[nums[i - k]] == 1:
                del only_arr[nums[i - k]]
            else:
                only_arr[nums[i - k]] -= 1
            temp = temp + nums[i] - nums[i - k]
            if len(only_arr) >= m:
                ret = max(ret, temp)
        return ret
    
nums = [1,2,1,2,1,2,1]
m = 3
k = 3
s = Solution()
print(s.maxSum(nums, m, k))