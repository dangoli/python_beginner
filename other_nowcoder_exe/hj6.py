import math

def isPrime(n): #判断是否为素数的函数 素数返回True 合数返回False
    n_root = int(math.sqrt(n))
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2, n_root + 1):
            if n % i == 0:
                return False
    return True

def divisor(p): # 求数的因子的函数，返回两个和最小的因子 list
    p_root = int(math.sqrt(p))
    j = [1, p]
    for i in range(p_root, 0, -1):
        if p % i != 0:
            pass
        else:
            j[0] = i
            break
    j[1] = int(p/(j[0]))
    if j[0] == 1:
        l = list()
        l.append(j[1])
        return l
    else:
        return j
    # return j

def bool_lst(lst):
    len_f = len(lst)
    i = 0
    for item in lst:
        if item:
            i += 1
    if i == len_f:
        return True
    else:
        return False
    
s = int(input()) # 接收输入的整数 int

lst = [s] # 存储待输出的质因子

len_lst = len(lst) # 待输出列表的长度 int

lst_flag = list() # 判断待输出列表是否全为质数的指标 全是质数则为True 默认不是质数 lst

for i in range(0, len_lst):
    lst_flag.append(isPrime(lst[i])) # 更新

lst_bool = bool_lst(lst_flag) # 更新 bool 

while (lst_bool == False): # 待输出因子列表中有合数
    for item in lst:
        s_new = divisor(item) # s_new是有两个因子的列表
        lst = lst + s_new # 在末尾加入两个因子
        lst.remove(item) # 删除被拆解的数
    len_lst = len(lst) # 更新len_lst
    lst_flag = list()
    for i in range(0, len_lst):
        lst_flag.append(isPrime(lst[i])) # 更新lst_flag
    lst_bool = bool_lst(lst_flag)

for item in lst:
    if item == 1:
        lst.remove(item)
lst.sort()

if lst_bool:
    print(" ".join(str(i) for i in lst))
# print(lst_flag)