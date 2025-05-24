# (1)创建字典
d = {10:'cat', 20:'dog', 30:'leehan', 20:'lin'}
print(d) # {10: 'cat', 20: 'lin', 30: 'leehan'} key相同时，会覆盖

# (2)zip函数
lst1 = [10, 20, 30, 40]
lst2 = ['cat', 'dog', 'leehan', 'junpyo', 'lin']
zipobj = zip(lst1, lst2)
print(zipobj) # 映射结果：zip对象
# print(list(zipobj)) # 1.用list()进行转换 [(10, 'cat'), (20, 'dog'), (30, 'leehan'), (40, 'junpyo')]
d = dict(zipobj)
print(d) # 输出字典类型 {10: 'cat', 20: 'dog', 30: 'leehan', 40: 'junpyo'}

# 使用参数创建字典
d = dict(cat = 10, dog = 20) # 赋值号左侧为key 右侧为value
print(d) # {'cat': 10, 'dog': 20}


t = (10, 20, 30) # 元组
print({t:10}) # t为key, 10为value {(10, 20, 30): 10}

# lst = [10, 20, 30] # 列表
# print({lst:10}) # TypeError: unhashable type: 'list' 报错 可变数据类型不可作key

# 字典属于序列
print('max:', max(d)) # max: dog 比较的是
print('min:', min(d)) # min: cat
print('len:', len(d)) # len: 2
# 字典的删除
del d
# print(d) # NameError: name 'd' is not defined. Did you mean: 'id'?
