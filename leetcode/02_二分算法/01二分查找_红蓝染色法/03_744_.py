from typing import List

def lower_bound(letters:List[str], target:int) -> int:
    # 返回第一个大于等于目标字母的ASCII值的字符的位置
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if ord(letters[mid]) < target:
            left = mid + 1
        else:
            right = mid - 1
    return left # 如果全都小于target，则left == len(letters)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = ord(target) + 1
        l = lower_bound(letters, n)
        if l == len(letters):
            return letters[0]
        else:
            return letters[l]


letters = ['c','f','j']
target = 'x'
s = Solution()
print(s.nextGreatestLetter(letters, target))