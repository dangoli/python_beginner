class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1 # 左移一位
            bit = n & 1 # 取出n的最低位
            res |= bit # 加到res的最低位
            n >>= 1 # n右移一位
        return res