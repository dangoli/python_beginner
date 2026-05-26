from typing import List
from itertools import accumulate
# 是首尾元音就是1，不是就是0，计算01数组的前缀和

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        is_yuanyin = lambda s: s[0] in 'aeiou' and s[-1] in 'aeiou'
        s = list(accumulate(map(is_yuanyin, words),initial = 0))
        return [s[r + 1] - s[l] for l, r in queries]