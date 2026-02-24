# 暴力枚举

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = {s[i - k: i] for i in range(k, len(s) + 1)}
        return len(st) == 1 << k