lst = [4, 56, 21, 11, 99]
print('原列表：', lst) 

# 排序
asc_lst = sorted(lst) #sorted()函数返回一个列表对象， 默认升序
print('升序：', asc_lst) # 升序： [4, 11, 21, 56, 99]
print('原列表：', lst) # 原列表： [4, 56, 21, 11, 99]

# 降序
desc_lst = sorted(lst, reverse=True)
print('降序：', desc_lst) # 降序： [99, 56, 21, 11, 4]
print('原列表：', lst) # 原列表： [4, 56, 21, 11, 99]

lst2 = ['jun', 'LEEHAN', 'gihyeon', 'Junpyo', 'Taesan']
print('原列表：', lst2) # 原列表： ['jun', 'LEEHAN', 'gihyeon', 'Junpyo', 'Taesan']

# 忽略大小写进行排序
new_lst2 = sorted(lst2, key=str.lower)
print('排序后的：', new_lst2) # 排序后的： ['gihyeon', 'jun', 'Junpyo', 'LEEHAN', 'Taesan']