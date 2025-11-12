from collections import Counter
from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky_num = []
        x = {}
        for i in nums:
            x[i] = x.get(i, 0) + 1
            if x[i] == 2:
                sneaky_num.append(i)
        return sneaky_num

nums = [0,3,2,1,3,2]
s = Solution()
print(s.getSneakyNumbers(nums))