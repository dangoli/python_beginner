import re
pattern = '\d\.\d+'
s = 'I study Python3.11 everyday Python2.7 i love you'
match = re.search(pattern, s)
print(match) # <re.Match object; span=(14, 18), match='3.11'>
s2 = '4.10 Python I study everyday'
match2 = re.search(pattern, s2)
print(match2) # <re.Match object; span=(0, 4), match='4.10'>
s3 = 'I study everyday'
match3 = re.search(pattern, s3)
print(match3) # None

print(match.group()) # 3.11
print(match2.group()) # 4.10