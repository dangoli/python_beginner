import math
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

lst = divisor(7)
print(lst)