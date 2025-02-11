# 使用()创建元组
t = ('hello', [10, 20, 30], 'python', 'world')
print(t) # ('hello', [10, 20, 30], 'python', 'world')

# 使用内置函数tuple()创建元组
t = tuple('helloworld')
print(t) # ('h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')

t = tuple([10, 20, 30, 40])
print(t) # (10, 20, 30, 40)
 
print('10在元组t中是否存在：', (10 in t))       # 10在元组t中是否存在： True
print('10在元组t中是否不存在：', (10 not in t)) # 10在元组t中是否不存在： False
print('最大值：', max(t)) # 最大值： 40
print('最小值：', min(t)) # 最小值： 10
print('len:', len(t)) # 长度 len: 4
print('t.index:', t.index(10)) # 10在元组中索引为0 t.index: 0
print('t.count:', t.count(10)) # 10的个数为 t.count: 1

# 如果元组中只有一个元素
t = (10)
print(t, type(t)) # 10 <class 'int'>

# 如果元组中只有一个元素 逗号不能省略
t = (10, )
print(t, type(t)) # (10,) <class 'tuple'>

# 元组的删除
del t
# print(t) # NameError: name 't' is not defined