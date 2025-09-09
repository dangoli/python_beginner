def fibonacci_custom(n): # 自定义斐波那契数列
    seq = [1, 1, 2, 3]  # 初始序列
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

fib31 = fibonacci_custom(31)
n = int(input())
print(fib31[n-1])