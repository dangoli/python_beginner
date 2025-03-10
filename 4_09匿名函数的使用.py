def calc(a, b):
    return a + b

print(calc(10, 20))

#匿名函数
s = lambda a, b:a + b # s表示一个匿名函数
print(type(s)) # <class 'function'>
# 调用匿名函数
print(s(10, 2))
print('-' * 16)
# 列表的正常取值操作
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    print(lst[i])
print()
print('-' * 16)

for i in range(len(lst)):
    result = lambda x:x[i] # 根据索引值，result类型为function，x是形参
    print(result(lst)) # lst是实参

#
stu_score = [
    {'name':'张三', 'score':88},
    {'name':'李四', 'score':93},
    {'name':'王五', 'score':98},
    {'name':'赵六', 'score':71}
]
# 对列表进行排序，排序的规则是字典的成绩
stu_score.sort(key=lambda x:x.get('score'), reverse=True) # 降序
print(stu_score)