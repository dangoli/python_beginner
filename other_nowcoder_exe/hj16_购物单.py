n, m = map(int, input().split()) # n为预算, m为物品总数
goods = [] # 存储商品信息的二维列表
for i in range(m):
    s = input()
    v, w, q = s.split(" ")
    tempv = int(v)
    tempw = int(w)
    tempq = int(q)
    goods.append([tempv, tempw, tempq])

numacc = [[0] * 4 for _ in range(m)] # 记录每个商品的附件数量与附件编号
for i in range(m): # 初始化
    numacc[i][0] = i

satis = [] # 存储商品的价格与满意度
for i in range(m):
    if goods[i][2] == 0: # 该商品是主件
        rec = i # 记录主件的下标
        tempv = goods[i][0]
        temps = goods[i][0] * goods[i][1] # 该组合商品的满意度
        satis.append([tempv, temps])
    else: # 该商品是附件
        recf = goods[i][2] - 1 # 记录该附件的主件的下标
        numacc[recf][1] += 1
        tempv = goods[i][0] + goods[recf][0] # 该组合商品的价格
        temps = goods[i][0] * goods[i][1] + goods[recf][0] * goods[recf][1]
        satis.append([tempv, temps])
        if numacc[recf][1] == 1: # 该附件是主件的第一个附件
            numacc[recf][2] = i # 记录该附件的下标
        else: # 该附件是主件的第二个附件
            numacc[recf][3] = i # 记录该附件的下标
            recacc = numacc[recf][2] # 第一个附件的下标
            tempv = goods[recf][0] + goods[recacc][0] + goods[i][0] # 该组合商品的价格
            temps = goods[recf][0] * goods[recf][1] + goods[recacc][0] * goods[recacc][1] + goods[i][0] * goods[i][1]
            satis.append([tempv, temps])

# 转化成01背包问题
num = len(satis) # 组合的数量(n)
bud = int(n/10) # 预算,减少计算量
satis_v = [0] * num
satis_w = [0] * num
for i in range(num):
    satis_v[i] = int(satis[i][0] / 10) # 组合价格除以10
    satis_w[i] = satis[i][1] # 组合满意度

dp = [[0] * (bud + 1) for _ in range(num)] # n行c+1列的二维数组，dp[i][j]表示前i个物品在容量为j的背包中能获得的最大价值\
# 初始化
for j in range(bud + 1):
    if j >= satis_v[0]:
        dp[0][j] = satis_w[0]

# 遍历组合
for i in range(1, num):
    for j in range(bud + 1):
        if j < satis_v[i]: # 如果当前预算小于组合价格，则不能加入该组合
            dp[i][j] = dp[i - 1][j] # 不能放入该物品，则最大价值为前i-1个物品的最大价值
        else: # 如果当前背包容量大于等于物品体积，则可以选择放入或不放入该物品
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - new_satis[i][0]] + new_satis[i][1])