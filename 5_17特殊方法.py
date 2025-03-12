a = 1
b = 2
print(dir(a)) # 查看a对象的所有方法
print(a + b) # 3
print(a.__add__(b)) # 3
print(a.__sub__(b)) # 执行减法运算
print(f'{a}<{b}吗？', a.__lt__(b)) # True
print(f'{a}<={b}吗？', a.__le__(b)) # True
print(f'{a}=={b}吗？', a.__eq__(b)) # False
print('-' * 16)
print(f'{a}>{b}吗？', a.__gt__(b)) # False
print(f'{a}>={b}吗？', a.__ge__(b)) # False
print(f'{a}!={b}吗？', a.__ne__(b)) # True
#
print('-' * 16)
print(a.__mul__(b)) # 乘法
print(a.__truediv__(b)) # 除法
print(a.__mod__(b)) # 取模
print(a.__floordiv__(b)) # 取整
print(a.__pow__(b)) # 幂运算