import random
lst = [item for item in range(1, 11)]
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [item * item for item in range(1, 11)]
print(lst) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst = [random.randint(1, 100) for _ in range(10)]
print(lst) # [43, 34, 8, 23, 9, 25, 93, 92, 97, 1]

# 从列表中选择符合条件的元素组成新列表
lst = [i for i in range(10) if i%2 == 0]
print(lst) # 筛选偶数出来组成列表 [0, 2, 4, 6, 8]