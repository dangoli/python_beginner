# 创建二维列表
lst = [
    ['城市', '环比', '同比'],
    ['北京', '102', '103'],
    ['上海', '104', '504'],
    ['深圳', '100', '39']
]
print(lst)

# 遍历二维列表用双重for循环
for row in lst: # 行
    for item in row: # 列
        print(item, end = '\t')
    print() 

# 列表生成式生成一个4行5列的二维列表
lst2 = [[ j for j in range(5)]for i in range(4)]
print(lst2) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]