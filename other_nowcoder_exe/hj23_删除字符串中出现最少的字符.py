"""
对于给定的仅包含小写字母的字符串，删除字符串中出现次数最少的字符. 输出删除后的字符串，要求保持其他字符的相对位置不变.
如果多个字符出现次数均为最少，则删除所有这些字符
输入描述:
在一行上输入一个长度为1到20的字符串, 仅包含小写字母
输出描述:
在一行上输出删除出现次数最少的字符后的字符串. 保证这个字符串至少包含一个字符
"""
from collections import Counter
s = input().strip()

count = Counter(s)
min_count = min(count.values())
result = ''.join([c for c in s if count[c] > min_count])
print(result)