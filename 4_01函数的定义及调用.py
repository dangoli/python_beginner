def get_sum(num): # 形式参数
    s = 0
    for i in range(1, num+1):
        s += i
    print(f'1到{num}之间的累加和为：{s}')

# 函数的调用
get_sum(10) # 实际参数
get_sum(100)
get_sum(1000)