import re # 导入
pattern = '\d\.\d+' # +限定符. \d 匹配数字 0-9数字出现1or多次
s = 'I study Python 3.10.11 everyday' # 待匹配字符串
match = re.match(pattern, s, re.I)
print(match) # None 未匹配到数字
s2 = '3.10.11Python I study everyday' 
match2 = re.match(pattern, s2)
print(match2) # <re.Match object; span=(0, 4), match='3.10'>

print('匹配值的起始位置：', match2.start())
print('匹配值的结束位置：', match2.end())
print('匹配区间的位置元素：', match2.span())
print('待匹配的字符串：', match2.string)
print('匹配的数据：', match2.group())