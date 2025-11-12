from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        sort_nums = sorted(nums)
        n = len(nums)
        len_w = 0
        i = j = 0 # 窗口左指针
        while j < n:
            if sort_nums[j] <= sort_nums[i] * k:
                len_w = max(len_w, j - i + 1)
                j += 1
            else:
                i += 1
        return n - len_w

nums = [8,99,65,16,39]
k = 3
s = Solution()
print(s.minRemoval(nums, k))