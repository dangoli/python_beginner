n=int(input())
a={}
for i in range(n):
    d=input().split()
    k=int(d[0])
    v=int(d[1])
    if k in a:
        a[k]+=v
    else:
        a[k]=v
b=sorted(a)
for key in range(len(b)):
    print(b[key],end=' ')
    print(a[b[key]])