from typing import List
from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        suf_cnt = Counter(s[1:])
        pre_set = set()
        st = set()
        for j in range(1, len(s) - 1): # 枚举中间j
            mid = s[j]
            suf_cnt[mid] -= 1
            if suf_cnt[mid] == 0:
                del suf_cnt[mid]
            pre_set.add(s[j-1])
            for alpha in pre_set &  suf_cnt.keys():
                st.add(alpha + mid)
        return len(st)