s = 'cdabcdabb'
print(s.split('ab'))
print('-' * 32)
word = '三更灯火五更鸡，正是男儿读书时'
print(word.index('正是男儿读书时')) # 8
print(word.find('黑发不知勤学早')) # -1
# print(word.index('白首方悔读书迟'))
print('-' * 32)
s1 = '中国梦'
lst = ['伟大', '美丽']
s3 = s1.join(lst)
print(s3)

print('-' * 32)
import re
pattern = r'13[4-9]\d{8}'
lst = ['13809876543', '15109876543', '13278965439', '15912345665', '13198765432']
for item in lst:
    match = re.match(pattern, item)
    if match != None:
        print(match.group())

print('-' * 32)
pattern = r'ysj_\w+'
s = 'ysj_python ysj_spider'
match = re.search(pattern, s) # 只查找到符合条件的第一个
print(match.group()) 

pattern = r'\s*@'
s = '@杨淑娟 @刘梅梅 @郭小川'
lst = re.split(pattern, s)
print(lst)