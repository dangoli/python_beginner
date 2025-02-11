d = {'hello':10, 'world':20, 'python':30}
# 访问字典元素
# (1)使用d[key]
print(d['hello']) # 10
# (2)d.get(key)
print(d.get('hello')) # 10

# 两者有区别：若key不存在，d[key]将报错，d.get(key)可指定默认值
# print(d['java']) # KeyError: 'java'
print(d.get('java')) # None
print(d.get('java', '不存在')) # 不存在


# 字典的遍历
for item in d.items():
    print(item) # 得到元组 key,value
# ('hello', 10)
# ('world', 20)
# ('python', 30)

# 在使用for循环遍历时，分别获取key，value
for key, value in d.items():
    print(key, '--->', value)
# hello ---> 10
# world ---> 20
# python ---> 30