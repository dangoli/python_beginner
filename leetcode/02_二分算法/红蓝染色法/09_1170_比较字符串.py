from typing import List
def f(s:str) -> int: # 时间复杂度 O(n) n为字符串长
    small = min(s)
    return s.count(small)

def lower_bound(nums:List[int], target:int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left # 找不到第一个大于等于目标的元素就返回数组nums长

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i, s in enumerate(queries):
            queries[i] = f(s)
        for i, s in enumerate(words):
            words[i] = f(s)
        words.sort() # 时间复杂度 O(m log m) m为words长度
        # 在words中找大于queries[i]的个数，返回 len - 下标
        for i, n in enumerate(queries):
            queries[i] = len(words) - lower_bound(words, n + 1)
        return queries
    
queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
s = Solution()
print(s.numSmallerByFrequency(queries, words))