import re
pattern = '\d\.\d+'
s = 'I study Python3.11 everyday Python2.7 i love you'
lst = re.findall(pattern, s)
print(lst) # 
s2 = '4.10 Python I study everyday'
lst2 = re.findall(pattern, s2)
print(lst2) # 
s3 = 'I study everyday'
lst3 = re.findall(pattern, s3)
print(lst3) # 