# 检查数组模k后的余数，
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = [0] * k
        for num in arr:
            mod[num % k] += 1
        if any(mod[i] != mod[k - i] for i in range(1, k // 2 + 1)):
            return False
        
        return mod[0] % 2 == 0

        
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
s = Solution()
print(s.canArrange(arr, k))