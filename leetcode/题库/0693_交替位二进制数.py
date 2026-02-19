# 直接遍历二进制位

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1 # 记录当前位
        n >>= 1 # 
        while n:
            cur = n & 1
            if cur == prev:
                return False
            prev = cur
            n >>= 1
        return True