# 序列
# 使用索引检索字符串的元素
# 正向索引
s = 'hello world'
for i in range(0, len(s)):
    print(i, s[i], end = '\t')
print('\n----------------')

# 反向递减
for i in range(-11, 0):
    print(i, s[i], end = '\t')
print('\n----------------')
print(s[10])
print()
print(s[-1])