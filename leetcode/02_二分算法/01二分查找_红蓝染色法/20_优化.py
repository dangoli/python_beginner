from typing import List
from bisect import bisect_left
from itertools import accumulate

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        # 累加属性矩阵
        increase = list(accumulate(increase, func=lambda prev, curr: [p + c for p, c in zip(prev, curr)]))
        # 初始化-1
        ans = [-1] * len(requirements)
        increase = list(zip(*increase)) # 转置，为了方便匹配

        for i, item in enumerate(requirements):
            if item == [0, 0, 0]:
                ans[i] = 0 # 第0天直接解锁
            else:
                j = bisect_left(increase[0], item[0])
                p = bisect_left(increase[1], item[1])
                q = bisect_left(increase[2], item[2])

                if j < len(increase[0]) and p < len(increase[0]) and q < len(increase[0]): # 等于len表示属性值太大，无法解锁
                    ans[i] = max(j, p, q) + 1
        return ans

increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]] 
requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
s = Solution()
print(s.getTriggerTime(increase, requirements))