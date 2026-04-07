# 对word排序去重
from typing import List
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for word in words:
            word = ''.join(sorted(set(word)))
            ans += cnt[word]
            cnt[word] += 1
        return ans
    
words = ["aba","aabb","abcd","bac","aabc"]
s = Solution()
print(s.similarPairs(words))