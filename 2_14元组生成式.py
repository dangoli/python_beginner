t = (i for i in range(1,4))
print(t) # <generator object <genexpr> at 0x000002C864B94120> 生成器对象

# t = tuple(t)
# print(t) # (1, 2, 3)

# 遍历
# for item in t:
#     print(item)

# __next__ 先注释掉for遍历
print(t.__next__()) #
print(t.__next__())
print(t.__next__()) 

t = tuple(t)
print(t) # 使用__next__已经取出元组t中所有元素了 # ()