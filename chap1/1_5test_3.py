# 使用嵌套循环输出九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j), end='\t')
    print()