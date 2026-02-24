"""
给定一个包含非负整数的数组nums, 返回其中可以组成三角形三条边的三元组的个数.
示例1:
输入: nums = [2,2,3,4]
输出: 3
示例2:
输入: nums = [4,2,3,4]
输出: 4
"""

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(2, n):
            i, j =0, k -1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j-i 
                    j -= 1
                else:
                    i += 1
        return count
