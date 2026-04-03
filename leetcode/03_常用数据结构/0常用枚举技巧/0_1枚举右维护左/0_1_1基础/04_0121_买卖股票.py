from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minPrice = prices[0]
        for j in prices:
            if j < minPrice:
                minPrice = j
            ans = max(j - minPrice,ans)

        return ans
    
nums = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(nums))