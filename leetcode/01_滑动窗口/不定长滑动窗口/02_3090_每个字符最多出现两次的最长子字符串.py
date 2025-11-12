from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l = 0
        max_l = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            # 当某字符超2次，移动左指针
            while count[ch] > 2:
                count[s[l]] -= 1
                l += 1
            max_l = max(max_l, r-l + 1)
        return max_l

s = "ccbbbcba"
solution = Solution()
print(solution.maximumLengthSubstring(s))