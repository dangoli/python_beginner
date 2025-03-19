import random
d = {item: random.randint(1, 100) for item in range(4)}
print(d) # {0: 68, 1: 75, 2: 99, 3: 23}

# 创建两个列表
lst = [1001, 1002, 1003]
lst2 = ['JunHwi', 'Ran', 'MiYeon']
d = {key:value for key, value in zip(lst, lst2)}
print(d) # {1001: 'JunHwi', 1002: 'Ran', 1003: 'MiYeon'}