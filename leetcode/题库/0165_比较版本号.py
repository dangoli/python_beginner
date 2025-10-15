"""
给定两个版本号 version1 和 version2, 比较它们. 版本号由一个或多个修订号组成, 修订号由一个或多个数字组成. 修订号之间用 '.' 连接. 
每个修订号可能包含前导零. 修订号的值是它转换为整数 并忽略前导零.
比较版本号时, 逐个比较从左到右的修订号. 如果其中一个版本字符串的修订号较少, 则在比较时将其后面的修订号视为 0.
返回规则如下:
- 如果 version1 > version2 返回 1,
- 如果 version1 < version2 返回 -1,
- 除此之外返回 0.
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n1, n2 = len(v1), len(v2)
        for i in range(max(n1, n2)):
            num1 = v1[i] if i < n1 else 0 # 缺失部分补0
            num2 = v2[i] if i < n2 else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
    
