s = {10, 20, 30}
# 向集合中添加元素
s.add(100)
print(s) # {100, 10, 20, 30}
# 删除元素
s.remove(20)
print(s) # {100, 10, 30}
# 清空集合
# s.clear()
# print(s)

# 集合的遍历
for item in s:
    print(item)

# 使用enumerate()函数遍历
for index, item in enumerate(s):
    print(index, '-->', item)

# 集合的生成式
s = {i for i in range(1, 10)}
print(s) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

s = {i for i in range(1, 10) if i%2 == 1}
print(s) # {1, 3, 5, 7, 9}