from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay) # 最多可以获得的花朵数量
        if m * k > n:
            return -1
        
        left = min(bloomDay) - 1
        right = max(bloomDay)

        def check(bloomDay: List[int], m: int, k: int, limit: int) -> bool:
            total = 0 # 总共可以制作的花束
            cur_cnt = 0 # 当前连续开放的花朵数目
            for day in bloomDay:
                if day > limit:
                    cur_cnt = 0
                else:
                    cur_cnt += 1
                if cur_cnt >= k:
                    total += 1
                    cur_cnt = 0
            return total >= m
        
        while left + 1 < right:
            mid = (left + right) >> 1
            if check(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid
        return right
    
bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2
s = Solution()
print(s.minDays(bloomDay, m, k))