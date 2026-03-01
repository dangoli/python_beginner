# 数学公式

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 0
        w = 1
        while (1 << (w - 1)) <= n:
            l = 1 << (w - 1)
            r = min((1 << w) - 1, n)
            m = r - l + 1
            q = 1 << w
            pow_q = pow(q, m, MOD)
            inv_q1 = pow(q - 1, -1, MOD)
            s = r * (pow_q - 1) * inv_q1 - (q - m * pow_q + (m - 1) * pow_q * q) * inv_q1 * inv_q1
            ans = ans * pow_q + s
            w += 1
        return ans % MOD