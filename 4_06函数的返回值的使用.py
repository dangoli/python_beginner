# 函数的返回值
def calc(a, b):
    print(a+b)

calc(1, 2)
print(calc(1, 2))
print('-' * 16)

def calc2(a, b):
    s = a + b
    return s 

get_s = calc2(2, 3)
print(get_s)

get_s2 = calc2(calc2(2, 3), 4)
print(get_s2)

# 
def get_sum(num):
    s = 0 # 累加和
    odd_sum = 0 # 奇数和
    even_sum = 0 # 偶数和
    for i in range(1, num+1):
        if i%2 != 0:  # 奇数
            odd_sum += i
        else:
            even_sum += i
        s += i
    return odd_sum, even_sum, s

result = get_sum(10)
print(type(result))
print(result)

# 解包赋值
a, b, c = get_sum(10) 
print(a)
print(b)
print(c)