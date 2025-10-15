from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        ans = float('-inf')
        # 从后往前
        for i in range(n-1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
            ans = max(ans, dp[i])
        return ans

energy = [5, 2, -10, -5, 1]
k = 3
s = Solution()
print(s.maximumEnergy(energy, k))