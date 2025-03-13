import random
# 设置随机数种子
random.seed(10) # 设置随机数种子为10
print(random.random()) # 0.5714025946899135 输出种子为10的随机数 范围[0,1)
random.seed(20) # 设置随机数种子为20
print(random.random()) # 0.9056396761745207 输出种子为20的随机数
print('-'*20)
random.seed(10) # 设置随机数种子为10
print(random.randint(1, 100)) # 74 输出种子为10的随机整数 范围[1,100]

for i in range(10):
    print(random.randrange(1, 10, 2)) # 输出种子为10的随机整数 范围[1,10) 步长为2

print('-'*20)
print(random.uniform(1, 100)) # 1.0000000000000002 输出种子为10的随机浮点数 范围[1,100)

lst = [i for i in range(1, 11)]
print(random.choice(lst)) # 5 输出种子为10的随机选择列表中的元素

# 随机的排序
random.seed(20) # 设置随机数种子为20
random.shuffle(lst) # 随机的排序
print(lst) # [3, 1, 6, 2, 10, 5, 4, 9, 7, 8] 输出种子为20的随机排序后的列表