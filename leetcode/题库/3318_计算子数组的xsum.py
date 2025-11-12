from typing import List
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        l = len(nums) - k + 1
        ans = []
        for i in range(l):
            n_nums = nums[i:i+k]
            count = Counter(sorted(n_nums, reverse=True))
            if len(count) < x:
                x_sum = sum(n_nums)
                ans.append(x_sum)
            else:
                x_sum = 0
                for j in range(x):
                    key = count.most_common()[j][0]
                    x_sum += key * count[key]
                ans.append(x_sum)
        return ans

nums = [9,2,2]
k = 3
x = 3
s = Solution()
print(s.findXSum(nums, k, x))