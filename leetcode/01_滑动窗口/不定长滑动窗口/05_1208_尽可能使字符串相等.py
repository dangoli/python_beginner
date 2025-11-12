class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_l = 0
        l = 0
        cost = 0
        for r, ch in enumerate(s):
            cost += abs(ord(ch) - ord(t[r]))
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            max_l = max(max_l, r - l + 1)
        return max_l
    
s = "abcd"
t = "bcdf"
maxCost = 3
solution = Solution()
print(solution.equalSubstring(s, t, maxCost))