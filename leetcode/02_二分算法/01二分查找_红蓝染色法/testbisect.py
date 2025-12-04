from bisect import bisect_left, bisect_right

nums = [1,2,4,4,7,9,10]
x = 9
print(bisect_left(nums, x))
print(bisect_right(nums, x))