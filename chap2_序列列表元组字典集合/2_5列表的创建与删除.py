lst = ['hello', 'world', 98, 100.5]
print(lst) # ['hello', 'world', 98, 100.5]

# 内置函数list()创建列表
lst2 = list('helloworld')
print(lst2) # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
lst3 = list(range(1,10,2)) #从1 到10,步长为2，不包含10
print(lst3) # [1, 3, 5, 7, 9]

print(lst + lst2 + lst3) # ['hello', 'world', 98, 100.5, 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 1, 3, 5, 7, 9]
print(lst * 3)
print(len(lst)) #4
print(max(lst3)) #9
print(min(lst3)) #1

print(lst2.count('o')) # 统计o的个数 2
print(lst2.index('o')) # o首次出现的位置 4

# 列表的删除
lst4 = [10, 20, 30]
print(lst4) # [10, 20, 30]
del lst4
