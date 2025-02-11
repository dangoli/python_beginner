lst = ['hello', 'world', 'python', 'php']

# 使用for循环遍历列表元素
for item in lst:
    print(item)

# 使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0, len(lst)):
    print(i, '-->', lst[i])

# enumearte()函数
for index, item in enumerate(lst):
    print(index, item) # index是序号，不是索引 0123

#手动修改序号的起始值
for index, item in enumerate(lst, start=1):
    print(index, item) # index 1234

for  index, item in enumerate(lst, 2):
    print(index, item) # 2345