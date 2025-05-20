n, m = map(int, input().split()) # n为预算, m为物品总数
goods = [] # 存储商品信息的二维列表
for i in range(m):
    s = input()
    v, w, q = s.split(" ")
    tempv = int(v)
    tempw = int(w)
    tempq = int(q)
    goods.append([tempv, tempw, tempq])
satis = [] # 存储商品的价格与满意度
for i in range(m):
    if goods[i][2] == 0: # 该商品是主件
        rec = i # 记录主件的下标
        tempv = goods[i][0]
        temps = goods[i][0] * goods[i][1] # 该组合商品的满意度
        satis.append([tempv, temps])
    else: # 该商品是附件
        recf = goods[i][2] - 1 # 记录该附件的主件的下标
        tempv = goods[i][0] + goods[recf][0] # 该组合商品的价格
        temps = goods[i][0] * goods[i][1] + goods[recf][0] * goods[recf][1]
        satis.append([tempv, temps])