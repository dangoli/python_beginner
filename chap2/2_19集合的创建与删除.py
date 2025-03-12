# {}直接创建集合
s = {10, 20, 30, 40} # 不可变数据类型
print(s) # {40, 10, 20, 30}
# 集合只能存储不可变数据类型 如果用列表(可变数据)作集合元素
# s = {[10, 20], [30, 40]}
# print(s) # TypeError: unhashable type: 'list' 报错：列表不可哈希

# 使用set()创建集合
s = set() # 创建了一个空集合 False
print(s) # set()
s = {} # 创建的是集合还是字典？ 字典
print(s, type(s)) # {} <class 'dict'>

s = set('helloworld')
print(s) # {'e', 'r', 'o', 'l', 'w', 'd', 'h'} 无序且不重复

s2 = set([10, 20, 30])
print(s2) # {10, 20, 30}

s3 = set(range(1, 10))
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 集合属于序列的一种
print('max:', max(s3)) # max: 9
print('min:', min(s3)) # min: 1
print('len:', len(s3)) # len: 9

print('9在集合中存在吗', (9 in s3)) # 9在集合中存在吗 True
print('9在集合中不存在吗', (9 not in s3)) # 9在集合中不存在吗 False

# 集合的删除
del s3
# print(s3) # NameError: name 's3' is not defined.