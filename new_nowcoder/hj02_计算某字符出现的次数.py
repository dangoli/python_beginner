"""
s = input()
c = input()

s_lower = s.lower()
c_lower = c.lower()
ccount = 0
for t in s_lower:
    if t == c_lower:
        ccount += 1

print(ccount)
"""

class Solution:
    def charcount(self, s : str, c : str) -> int:
        s_l = s.lower()
        c_l = c.lower()
        ccount = 0
        for t in s_l:
            if t == c_l:
                ccount += 1

        return ccount

s = input()
c = input()
s1 = Solution()
print(s1.charcount(s, c))