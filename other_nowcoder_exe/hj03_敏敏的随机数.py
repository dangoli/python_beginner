import random
n = int(input())
s = set() # 创建集合s
for i in range(0, n):
    j = int(input())
    s.add(j)

lst = list() # 创建列表
for item in s:
    lst.append(item)

lst.sort()

for item in lst:
    print(item)