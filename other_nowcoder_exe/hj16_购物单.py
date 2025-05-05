n, m = map(int, input().split())
# n, m =
goods = [] # 存储商品信息的二维列表
for i in range(m):
    s = input()
    v, w, q = s.split(" ")
    tempv = int(v)
    tempw = int(w)
    tempq = int(q)
    goods.append([tempv, tempw, tempq])
