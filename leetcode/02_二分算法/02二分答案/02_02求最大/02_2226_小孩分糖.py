from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: # 不够分的
            return 0
        left = 0
        right = min(max(candies), sum(candies) // k) + 1 # right不一定取最小的糖果推堆        
        # 开区间写法
        while left + 1 < right:
            mid = (left + right) >> 1
            if sum(c//mid for c in candies) >= k:
                left = mid
            else:
                right = mid
        return left
    
candies = [5,8,6]
k = 3
s = Solution()
print(s.maximumCandies(candies,k))