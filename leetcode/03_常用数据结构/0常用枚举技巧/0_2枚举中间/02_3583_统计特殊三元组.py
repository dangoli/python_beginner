from typing import List
from collections import Counter
from collections import defaultdict
# 遍历中间

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        suf = Counter(nums)

        ans = 0
        pre = defaultdict(int)
        for x in nums:
            suf[x] -= 1 # 去掉前面的
            ans += pre[x * 2] * suf[x * 2]
            pre[x] += 1
        return ans % MOD