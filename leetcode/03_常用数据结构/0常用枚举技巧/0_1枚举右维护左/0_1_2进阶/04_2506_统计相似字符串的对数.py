from collections import defaultdict
from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for word in words:
            mask = 0 # 记录字母出现否
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            ans += cnt[mask]
            cnt[mask] += 1
        return ans
    
words = ["aba","aabb","abcd","bac","aabc"]
s = Solution()
print(s.similarPairs(words))