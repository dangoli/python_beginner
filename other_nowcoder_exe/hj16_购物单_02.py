m, n = map(int, input().split()) # n为预算, m为物品总数
items = [] # 存储商品信息的二维列表
for _ in range(m):
    v, p, q = map(int, input().split()) # 分别是价格、重要度、主件编号
    items.append((v, p, q))

main_items = {}  # 主件的字典，键为输入中的索引（1-based）
attachments = []  # 附件列表，元素为(q, v, p) 主件编号、价格、重要度

for idx in range(m):
    v, p, q = items[idx]
    if q == 0: #该商品是主件
        main_item_idx = idx + 1  # 主件在输入中的索引（1-based）
        main_items[main_item_idx] = {
            'v': v, # 价格
            'p': p, # 重要度
            'attachments': [] # 附件列表
        }
    else: #该商品是附件
        attachments.append((q, v, p))

# 将附件添加到对应的主件中
for q, v, p in attachments:
    if q in main_items:
        main_items[q]['attachments'].append((v, p))

# 生成每个主件的所有可能选项
groups = []
for mi in main_items.values():
    v = mi['v']
    p = mi['p']
    attachments = mi['attachments']
    t = len(attachments)
    options = []
    for mask in range(1 << t):
        current_v = v
        current_s = v * p
        for i in range(t):
            if mask & (1 << i):
                current_v += attachments[i][0]
                current_s += attachments[i][0] * attachments[i][1]
        options.append((current_v, current_s))
    groups.append(options)

# 动态规划处理分组背包问题
dp = [0] * (n + 1)
for options in groups:
    temp = dp.copy()
    for cost, value in options:
        for j in range(n, cost - 1, -1):
            if temp[j - cost] + value > dp[j]:
                dp[j] = temp[j - cost] + value

print(dp[n])