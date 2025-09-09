import math
s = int(input())
# flag = True # 判断是否为素数，素数返回True
def isPrime(n):
    n_root = int(math.sqrt(n))
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2, n_root + 1):
            if n % i == 0:
                return False
    return True # 遍历结束，为素数

# 递归算法？
def prime(p):  
    p_root = int(math.sqrt(p))
    j = [0, 0]
    for i in range(p_root, 0, -1):
        if p % i != 0:
            pass
        else:
            j[0] = i
            break
    j[1] = int(p/(j[0]))
    return j

flag = isPrime(s) # 判断输入的数是否为素数，若是则返回True
if flag:
    print(s)
else:
    m = prime(s)
m = prime(s) # s是待分解的整数，m是存储分解后的列表，存有两个因数
for i in range(0, 2):
    pass
print(m)