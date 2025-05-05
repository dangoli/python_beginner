def length_of_LIS(nums): # 优化后的算法 倒着来 时间复杂度 O(n^2)
    n = len(nums) 
    L = [1] * n # initial value [1, 1, ……, 1] 记录位置i开始的最长递增子序列长度

    for i in reversed(range(n)): # i -> n-1, n-2, …… , 2, 1, 0
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)
    
    return max(L)

nums = [1, 5, 2, 4, 3]
print(length_of_LIS(nums))