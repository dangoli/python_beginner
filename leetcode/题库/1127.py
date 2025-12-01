from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # min_prefix[r] 存储 index % k == r 时的最小前缀和
        min_prefix = [0] * k
        curr_sum = 0
        
        # 预处理前 k 个元素
        for i in range(k):
            curr_sum += nums[i]
            min_prefix[i] = curr_sum
        
        ans = min_prefix[-1]
        # 修正边界
        if min_prefix[-1] > 0:
            min_prefix[-1] = 0
            
        # 遍历剩余元素
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            remainder = i % k
            
            # 尝试更新最大值：当前前缀和 - 同余数的最小历史前缀和
            sub_sum = curr_sum - min_prefix[remainder]
            if sub_sum > ans:
                ans = sub_sum
            
            # 记录该余数下出现的最小前缀和
            if curr_sum < min_prefix[remainder]:
                min_prefix[remainder] = curr_sum
                
        return ans
