#
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}#创建一个空哈希表(字典)
        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x],j]
            idx[x] = j # 保存nums[j]和下标