from typing import List
# 报错

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
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        for i in range(len(queries)):
            n = nums[queries[i]] # nums 待找的数字
            p = []
            for l, num in enumerate(nums):
                if num == n:
                    p.append(l)
            if len(p) == 1:
                queries[i] = -1
            else:
                p.insert(0, p[-1] - len(nums))
                p.append(p[1] + len(nums))
                j = lower_bound(p, p[1])
                queries[i] = min(p[1] - p[j - 1], p[j + 1] - p[1])

        return queries


nums = [1,3,1,4,1,3,2] 
queries = [0,3,5]
s = Solution()
print(s.solveQueries(nums, queries))