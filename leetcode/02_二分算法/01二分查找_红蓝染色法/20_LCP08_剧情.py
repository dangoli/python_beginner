from typing import List

def binary_matrix(increase: List[int], col: int, target:int) -> int:
    m = len(increase)
    left, right = 0, m-1
    ans = m
    while left <= right:
        mid = (left + right) // 2
        value = increase[mid][col]
        if value >= target:
            ans = mid
            right = mid - 1
            return mid
        else:
            left = mid + 1
    return ans if ans < m else -1

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        increase = [[0,0,0]] + increase
        for i in range(1, len(increase)):
            for j in range(3):
                increase[i][j] += increase[i-1][j] #累加 
        ans = []
        for require in requirements:
            d0 = binary_matrix(increase, 0, require[0])
            d1 = binary_matrix(increase, 1, require[1])
            d2 = binary_matrix(increase, 2, require[2])
            if d0 != -1 and d1 != -1 and d2 != -1:
                ans.append(max(d0,d1,d2))
            else:
                ans.append(-1)
        return ans
    
increase = [[2,8,4],[2,5,0],[10,9,8]] 
requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]
s = Solution()
print(s.getTriggerTime(increase, requirements))
