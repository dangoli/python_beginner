from typing import List

def lower_bound(nums:List[int], target:int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left # 

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0] * len(spells)
        potions.sort()
        for i in range(len(spells)):
            n = (success + spells[i] - 1) // spells[i]
            pairs[i] = len(potions) - lower_bound(potions, n)
        return pairs
    
spells = [3,1,2]
potions = [8,5,8]
success = 16
s = Solution()
print(s.successfulPairs(spells, potions,success))