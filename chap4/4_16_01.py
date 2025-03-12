import random
def get_max(lst):
    x = lst[0] # x存储lst最大元素
    # 遍历
    for i in range(1, len(lst)):
        if lst[i] > x:
            x = lst[i] # 更新x
    return x

# 调用
lst = [random.randint(1, 100) for item in range(10)]
print(lst)
#计算最大值
smax = get_max(lst)
print(smax)