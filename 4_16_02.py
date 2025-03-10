# 编写函数实现提取指定字符串中的数字 并求和
def get_digit(x):
    s = 0 # 存储累加和
    lst = [] # 存储提取的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    # 求和
    s = sum(lst)
    return lst, s

# 准备函数的调用
s = input('输入一个字符串：')
# 调用
lst, x = get_digit(s)
print('提取的数字列表为：', lst)
print('累加和为：', x)