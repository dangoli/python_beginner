from typing import List
# 时间复杂度 O(n log n)

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

def calculate(nums:List[int], target:int) -> int:
    nums.sort() # 时间复杂度O(n log n)
    l_nums = 0
    for _ in nums:
        if _ > target:
            break
        else:
            l_nums += 1
            target -= _
    return l_nums

nums = [4,5,2,1]
target = 10
print(calculate(nums, target))