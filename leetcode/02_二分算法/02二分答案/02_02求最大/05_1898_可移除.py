from typing import List
# 1174ms

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable) + 1

        def check(x: int) -> bool:
            idx = set(removable[:x]) # 一定要改成set，list复杂度是O(x)
            it = (s[i] for i in range(len(s)) if i not in idx) # 创建一个生成器 `it`，用于遍历字符串 `s` 中未被移除的字符
            return all(c in it for c in p) # 使用 `all` 函数检查字符串 `p` 的每个字符 `c` 是否都存在于生成器 `it` 中
        
        while left + 1 < right:
            mid = (left + right) >> 1
            if check(mid):
                left = mid
            else:
                right = mid
        return left 
    
s = "qlevcvgzfpryiqlwy"
p = "qlecfqlw"
removable = [12,5]
s1 = Solution()
print(s1.maximumRemovals(s,p,removable))