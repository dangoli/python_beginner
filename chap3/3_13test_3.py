# 格式化输出商品的名称和单价
lst = [
    ['01', '电视', '小米', '13999'],
    ['02', '电冰箱', '美的', '8999'],
    ['03', 'Xbox', '微软', '4299']
]
print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i, end='\t\t')
    print()
print('-' * 32)
# 格式化
for item in lst:
    item[0] = '0000' + item[0]
    p = eval(item[3])
    item[3] = '￥{0:.2f}'.format(p)

print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i, end='\t\t')
    print()