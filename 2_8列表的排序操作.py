lst = [4, 56, 21, 11, 99]
print('原列表：', lst) # 原列表： [4, 56, 21, 11, 99]

# 排序，默认升序
lst.sort() # 不会产生新的列表对象，是在原列表上进行的
print('升序：', lst) # 升序： [4, 11, 21, 56, 99]

# 排序，降序
lst.sort(reverse=True)
print('降序：', lst) # 降序： [99, 56, 21, 11, 4]

print('-' * 16)
lst2 = ['GiHyeon', 'LEEHAN', 'TAESAN', 'LIN', 'JUNPYO']
print('原列表：', lst2) # 原列表： ['GiHyeon', 'LEEHAN', 'TAESAN', 'LIN', 'JUNPYO']

# 升序排序，按照ASCII码
lst2.sort()
print('升序：', lst2) # 升序： ['GiHyeon', 'JUNPYO', 'LEEHAN', 'LIN', 'TAESAN']

# 降序
lst2.sort(reverse=True)
print('降序：', lst2) # 降序： ['TAESAN', 'LIN', 'LEEHAN', 'JUNPYO', 'GiHyeon']

# 忽略大小写进行比较 自己制定规则
lst2.sort(key=str.lower) # 都转成小写 ????
print(lst2)