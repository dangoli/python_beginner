lst = [10, 20, 30, 40] # 列表
lst.append(('hello', 'world')) # append()函数向列表末尾添加元素， 添加元组
print(len(lst)) # 5

d = {'a':10, 'b':20, 'c':30, 'd':40} # 字典
d2 = d
d['b'] = 100
print(d['b'] + d2['b']) # 字典 引用传递 指向同一块地址 200

# 字典的键key必须是不可变数据类型

lst = [2008, 2019] # 列表
lst.append(2035) # 列表
lst.append(['2025', 2025]) # 列表
print(lst) # [2008, 2019, 2035, ['2025', 2025]]

lst = [] # 列表
for i in '想念':
    for j in '家人':
        lst.append(i + j)
print(lst) # ['想家', '想人', '念家', '念人']

lst = [1, 3, 5, 7]
lst.insert(2, 20) # 在列表指定位置插入元素
print(lst) # [1, 3, 20, 5, 7]

lst = [1, 3, 5, 7, 9]
print(lst.reverse()) # None reverse()函数用于列表数据的反转 函数无返回值

t = (10) # int类型
print(t, type(t))