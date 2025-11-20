from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dumpli_dict = defaultdict(int) # 创建一个带默认值的字典
        left = 0
        res = 0
        for r in range(len(answerKey)):
            dumpli_dict[answerKey[r]] += 1
            while dumpli_dict['T'] > k and dumpli_dict['F'] > k:
                dumpli_dict[answerKey[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        return res

answerKey = "TTFTTFTT"
k = 1
s = Solution()
print(s.maxConsecutiveAnswers(answerKey, k))