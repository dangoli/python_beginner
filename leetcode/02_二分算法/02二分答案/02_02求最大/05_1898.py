# 改写check函数, 更慢了
from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable) + 1

        def check(k: int) -> bool:
            removed = [False] * len(s)
            for i in range(k):
                removed[removable[i]] = True

            j = 0  # 指向 p
            for i in range(len(s)):
                if removed[i]:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1
                if j == len(p):
                    return True
            return j == len(p)
        
        while left + 1 < right:
            mid = (left + right) >> 1
            if check(mid):
                left = mid
            else:
                right = mid
        return left 