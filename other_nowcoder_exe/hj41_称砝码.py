n = int(input())
m = list(map(int, input().split()))
x = list(map(int, input().split()))

weights = {0}
for i in range(n):
    current = set()
    for w in weights:
        for k in range(1, x[i]+1):
            current.add(w + m[i]*k)
    weights |= current  # 合并新得到的重量
print(len(weights))