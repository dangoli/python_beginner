d = {1001:'李梅', 1002:'李涵', 1003:'李华'}
print(d) # {1001: '李梅', 1002: '李涵', 1003: '李华'}

# 字典，可变序列 向字典中添加元素
d[1004] = '张三'
print(d) # {1001: '李梅', 1002: '李涵', 1003: '李华', 1004: '张三'} 直接使用赋值运算符向字典添加元素

# 获取字典中所有的key
keys = d.keys()
print(keys) # dict_keys([1001, 1002, 1003, 1004])
print(list(keys)) # [1001, 1002, 1003, 1004]列表
print(tuple(keys)) # (1001, 1002, 1003, 1004)元组

# 获取字典中所有的value
values = d.values()
print(values) # dict_values(['李梅', '李涵', '李华', '张三'])
print(list(values)) # ['李梅', '李涵', '李华', '张三']
print(tuple(values)) # ('李梅', '李涵', '李华', '张三')

# 将字典中的数据转成key-value的形式，以元组的方式展现
lst = list(d.items())
print(lst)