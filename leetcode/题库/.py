from collections import Counter
from typing import List

class Solution: # 带记忆的动态规划
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power) # 统计每一种伤害值的总量
        keys = sorted(cnt.keys()) # 对伤害值排序
        n = len(keys)
        dp = [0] * n # 考虑到第i个不同伤害值时的最大伤害

        for i in range(n):
            cur = keys[i] * cnt[keys[i]]
            if i == 0:
                dp[i] = cur
            elif (keys[i] - keys[i-1] <= 2):
                dp[i] = max(dp[i-1], cur + (dp[i-2] if i >= 2 else 0))
            else:
                dp[i] = dp[i-1] + cur
        return dp[-1]
    
power = [5,9,2,10,2,7,10,9,3,8]
s = Solution()
print(s.maximumTotalDamage(power))