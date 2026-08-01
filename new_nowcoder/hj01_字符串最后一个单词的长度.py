import sys

class Solution:
    def lenoflastword(self, s : str) -> int:
        return len(s.split()[-1])

s = 'HELLONowcoder123'
q = Solution()
print(q.lenoflastword(s))

