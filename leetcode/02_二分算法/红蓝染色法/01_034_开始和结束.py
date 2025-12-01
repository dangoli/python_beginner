from typing import List

def lower_bound(nums:List[int], target:int) -> int:
    left = 0
    right = len(nums) - 1 # 闭区间[l, r]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def lower_bound2(nums:List[int], target:int) -> int:
    left = 0
    right = len(nums) # 左闭右开区间[l, r)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left # right也可以

def lower_bound3(nums:List[int], target:int) -> int:
    left = -1
    right = len(nums) #开区间(l, r)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid # (mid, right)
        else:
            right = mid
    return right

nums = [-1,0,3,5,9,12]
target = 13
print(lower_bound(nums, target))