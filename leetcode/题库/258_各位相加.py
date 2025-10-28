class Solution:
    def addDigits(self, num: int) -> int:
        # 用求数根公式 1 + (n-1)mod 9 当n非0
        return 1 + ((num - 1) % 9) if num != 0 else 0