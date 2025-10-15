from typing import List
from collections import Counter
# 用哈希表跟栈
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # 先初始化一个栈，将第一个单词入栈
        stack = [words[0]]

        for i in range(1, len(words)):
            # 检查与前一个单词是否异位词
            if Counter(words[i]) != Counter(stack[-1]):
                stack.append(words[i])

        return stack
    
words = ["abba","baba","bbaa","cd","cd"]
s = Solution()
print(s.removeAnagrams(words))