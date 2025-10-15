from itertools import pairwise

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        # write 指向下一个非异位词 应该被放置的位置
        write = 1

        # 相邻元素的元组
        for prev, cur in pairwise(words):
            # 检查两个相邻单词是否异位词
            if sorted(prev) != sorted(cur):
                # 如果不是异位词，就保留cur
                # 将cur放到write位置
                words[write] = cur
                # write指针后移，为下一个非字母异位词做准备
                write += 1
        # 删除列表末尾多余的元素
        del words[write:]

        return words
    
words = ["abba","baba","bbaa","cd","cd"]
s = Solution()
print(s.removeAnagrams(words))