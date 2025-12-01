# 转化成 找最后一个< target的位置再加上1
# 而找最后一个< target的位置 可以转化成 找第一个>= target的位置再减1
from typing import List
def lower_bound(nums:List[int], target:int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def searchInsert(self, nums:List[int], target:int) -> int:
        s = lower_bound(nums, target) - 1
        return s + 1
    
nums = [1,3,5,6]
target = 7
s = Solution()
print(s.searchInsert(nums, target))