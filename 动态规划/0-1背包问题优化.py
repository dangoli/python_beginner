# 滚动数组优化
# 物品总件数n，背包总空间大小为c，原本使用n行c+1列的二维数组来存储每个物品在每个背包容量下的最大价值，可以优化为2行c+1列,节省空间
# 只需要保存上一次的结果即可，当前行只依赖于上一行的结果

n = 4
c = 8
v = [4, 2, 3, 7] # 物品的体积
w = [51, 3, 4, 19] # 物品的价值
dp = [[0] * (c + 1) for _ in range(2)] # 2行c+1列的二维数组，dp[i][j]表示前i个物品在容量为j的背包中能获得的最大价值
# 初始化
for j in range(c + 1):
    if j >= v[0]:
        dp[0][j] = w[0]

# 遍历后续物品
for i in range(1, n):
    for j in range(c + 1):
        if j < v[i]:
            dp[i % 2][j] = dp[(i - 1) % 2][j]
        else:
            dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - v[i]] + w[i])

print(dp[(n - 1) % 2][c]) # 输出最大价值