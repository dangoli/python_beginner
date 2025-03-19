lst = ['hello', 'world', 'python']
print('原列表：', lst, id(lst)) # 原列表： ['hello', 'world', 'python'] 1483960360000

# 增加元素的操作
lst.append('sql')
print('加元素之后：', lst, id(lst)) # 元素之后： ['hello', 'world', 'python', 'sql'] 1483960360000

# 使用insert()函数在指定的index位置上插入元素x
lst.insert(1, 100)
print(lst) # ['hello', 100, 'world', 'python', 'sql']

# 列表元素的删除操作
lst.remove('world')
print('删除元素之后：', lst, id(lst))  # 删除元素之后： ['hello', 100, 'python', 'sql'] 1483960360000

# 使用pop(index) 根据索引将元素取出，然后删除
print(lst.pop(1)) # 100
print(lst) # ['hello', 'python', 'sql']

# 清楚列表中所有的元素clear()
# lst.clear()
# print(lst, id(lst)) # [] 2224119997248(每次debug都会重分配id)

# 列表的逆向输出
lst.reverse() # 不会产生新的列表，在原列表的基础上进行的
print(lst) # ['sql', 'python', 'hello']

# 列表的拷贝，将产生一个新的列表对象
new_lst = lst.copy()
print(lst, id(lst))         # ['sql', 'python', 'hello'] 2748207981376
print(new_lst, id(new_lst)) # ['sql', 'python', 'hello'] 2748207983104

# 列表元素的修改
lst[1] = 'mysql'
print(lst) # ['sql', 'mysql', 'hello']
