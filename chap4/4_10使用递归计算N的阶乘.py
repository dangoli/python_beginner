def fac(n): # n的阶乘
    if n == 1:
        return 1
    else:
        return n * fac(n-1) # 递归

print(fac(5)) # 