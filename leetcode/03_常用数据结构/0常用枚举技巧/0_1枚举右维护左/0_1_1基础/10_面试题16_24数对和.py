from typing import List
from collections import defaultdict

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cnt = defaultdict(int)
        for x in nums:
            if cnt[target - x]:
                cnt[target - x] -= 1
                ans.append([x, target - x])
            else:
                cnt[x] += 1
        return ans 
    

s = Solution()
print(s.pairSums([5,6,5], 11))