print('非空字符串的布尔值：', bool('hello')) # True
print('空字符串的布尔值：', bool('')) # 全是False
print('空列表的布尔值：', bool([]))
print('空列表的布尔值：', bool(list()))
print('空元组的布尔值：', bool(()))
print('空元组的布尔值：', bool(tuple()))
print('空集合的布尔值：', bool(set()))
print('空字典的布尔值：', bool({}))
print('空字典的布尔值：', bool(dict()))
print('-' * 16)
print('非0数值型的布尔值：', bool(123))
print('整数0的布尔值：', bool(0))
print('浮点数0.0的布尔值：', bool(0.0))

# 将其他类型转为字符串类型
lst = [1, 2, 3]
print(type(lst), lst) # <class 'list'> [1, 2, 3]

s = str(lst)
print(type(s), s) # <class 'str'> [1, 2, 3]

# float类型和str类型转成int类型
print('-' * 16, 'float类型和str类型转成int类型', '-' * 16)
print(int(98.7) + int('98'))
# 注意事项
#print(int('98.7')) # ValueError: invalid literal for int() with base 10: '98.7' 无效文本


print('-' * 16, 'int,str类型转成float类型', '-' * 16)
print(float(90) + float('3.14'))

s = 'hello' # <class 'str'>
print(list(s))

seq = range(1, 10) # <class 'range'>
print(tuple(seq))
print(set(seq))
print(list(seq))