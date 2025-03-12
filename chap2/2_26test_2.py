# 创建新列表，存储入库的商品信息
lst = []
for i in range(5):
    goods = input('请输入商品的编号和商品的名称进行商品入库，每次只可输入一件商品：')
    lst.append(goods)
# 输出所有商品信息
for item in lst:
    print(item)

# 创建空列表，存储购物车中商品
cart = []
while True:
    flag = False # 代表没有商品的情况
    num = input('请输入想购买的商品编号：')
    # 遍历商品列表，查询一下要购买的商品是否存在
    for item in lst:
        if num == item[0:4]: # 切片操作，从商品中切出序号
            flag = True
            cart.append(item) # 添加到购物车中
            print('商品已成功添加至购物车')
            break # 退出
    if not flag and num != 'q': # not flag 
        print('商品不存在')
    
    if num == 'q':
        break # 退出while循环
print('-' * 16)
print('您购物车已选择的商品为：')
cart.reverse()
for item in cart:
    print(item)