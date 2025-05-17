# 一维数组优化
n = 4
c = 9
v = [3, 1, 4, 6] # 物品的体积
w = [5, 7, 6, 4] # 物品的价值
dp = [0] * (c + 1) # 一维数组，dp[j]表示容量为j的背包中能获得的最大价值
# 初始化
for j in range(c + 1):
    if j >= v[0]:
        dp[j] = w[0]

# 遍历后续物品
for i in range(1, n):
    for j in range(c, v[i] - 1, -1): # 从后往前遍历，避免重复计算
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])

print(dp[c]) # 输出最大价值