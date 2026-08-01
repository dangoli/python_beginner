n = int(input())
s = set()
for i in range(0, n):
    j = int(input())
    s.add(j)

lst = list()
for item in s:
    lst.append(item)

lst.sort()

for i in lst:
    print(i)