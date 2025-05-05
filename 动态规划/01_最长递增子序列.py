# 动态规划：用空间换时间 带备忘录的递归 递归树的剪枝
memo = {} # 用哈希表存储已经得出的结果
def L(nums, i): # 暴力枚举法 时间复杂度 O(2*(2^n - 1))
    # 返回从位置i开始的最大递增子序列

    if i == len(nums) - 1: # 序列末尾
        return 1
    
    max_len = 1
    for j in range(i + 1, len(nums)): # 从i后面的数字开始检查
        if nums[j] > nums[i]: # 只要j指向的数字比i大
            max_len = max(max_len, L(nums, j) + 1) # 递归调用函数自身 计算从j开始的最长子序列

    memo[i] = max_len
    return max_len

def length_of_LIS(nums):
    return max(L(nums, i) for i in range(len(nums)))

nums = [1, 5, 2, 4, 3]
print(length_of_LIS(nums))