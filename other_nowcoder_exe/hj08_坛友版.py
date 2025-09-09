n = int(input())
a = {} #字典，存储合并索引后的表
for i in range(n):
    d = input().split()
    k = int(d[0]) # 存储接收的索引值 int
    v = int(d[1]) # 存储对应的数值
    if k in a:
        a[k] += v
    else:
        a[k] = v
b = sorted(a)
for key in range(len(b)):
    print(b[key], end=' ')
    print(a[b[key]])