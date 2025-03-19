s = 'hello world'
print('e在字符串s中存在吗？', ('e'in s)) # True
print('v在字符串s中存在吗？', ('v'in s)) # False

print('e在字符串s中不存在吗？', ('e'not in s)) # False
print('v在字符串s中不存在吗？', ('v'not in s)) # True

# 内置函数的使用
print('len():', len(s)) # 11
print('max():', max(s)) # w   按ASCII码值输出最大最小
print('min():', min(s)) #  (空格)

# 序列对象的方法 使用序列的名称打点调用
print('s.index():', s.index('o')) # o在字符串s中第一次出现的索引位置 4
# print('s.index():', s.index('v')) # 报错：substring not found 因为字符串s中不存在v 
print('s.count()', s.count('o')) #统计o在字符串s中出现的次数 2