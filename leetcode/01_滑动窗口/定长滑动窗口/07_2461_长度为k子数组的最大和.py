from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        only_dic = {}
        temp = 0
        for i in range(k):
            if nums[i] not in only_dic:
                only_dic[nums[i]] = 1
            else:
                only_dic[nums[i]] += 1
            temp += nums[i]
        ret = temp
        if len(only_dic) < k:
            ret = 0

        for i in range(k, len(nums)):
            if nums[i] in only_dic:
                only_dic[nums[i]] += 1
            else:
                only_dic[nums[i]] = 1
            if only_dic[nums[i-k]] == 1:
                del only_dic[nums[i-k]]
            else:
                only_dic[nums[i-k]] -= 1
            temp = temp + nums[i] - nums[i-k]
            if len(only_dic) == k:
                ret = max(ret, temp)
        return ret
        
nums = [1,1,1,7,8,9]
k = 3
s = Solution()
print(s.maximumSubarraySum(nums, k))