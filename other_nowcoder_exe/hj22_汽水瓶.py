"""
递归问题
三个空汽水瓶可以换一瓶汽水, 允许向老板借空汽水瓶, 但必须还. 有n个空汽水瓶, 最多可以喝多少瓶汽水?
"""
def max_drink(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return n // 3 + max_drink(n // 3 + n % 3)
    
while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(max_drink(n))
    except:
        break