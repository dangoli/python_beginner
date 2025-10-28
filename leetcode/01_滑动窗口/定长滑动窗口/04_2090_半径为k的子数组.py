from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n_ave = [-1] * len(nums)
        s = sum(nums[:k + k + 1])
        for i in range(k, len(nums) - k):
            n_ave[i] = s // (2 * k + 1)
            s = s - nums[i - k] + nums[i + k + 1] if i + k + 1 < len(nums) else s
        return n_ave
nums = [7,4,3,9,1,8,5,2,6]
k = 3
s = Solution()
print(s.getAverages(nums, k))

nums = [100000]
k = 0 
s = Solution()
print(s.getAverages(nums, k))