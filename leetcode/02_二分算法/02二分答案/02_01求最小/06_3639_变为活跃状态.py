from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        if n * (n+1) // 2 < k:
            return -1
        star = [0] * n # 记录已经变成星号的位置下标
        def check(m: int) -> bool:
            m += 1
            for j in range(m):
                star[order[j]] = m
            cnt = 0
            last = -1
            for i, x in enumerate(star):
                if x == m:
                    last = i
                cnt += last + 1
                if cnt >= k:
                    return True
            return False

        left, right = -1, n-1
        while left + 1< right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

s = "abc" 
order = [1,0,2]
k = 2
so = Solution()
print(so.minTime(s, order, k))