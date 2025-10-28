# zip的使用
a = [1,2,3]
b = ['a','b','c']

zipped = zip(a,b) # 返回一个迭代器 把多个序列按照位置配对形成一个个元组
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 长度不等时 以最短的序列为准
c = ['x','y']
print(list(zip(a,b,c))) # [(1, 'a', 'x'), (2, 'b', 'y')]

# 可以用*操作符解压
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)
print(nums) # (1, 2, 3)
print(letters) # ('a', 'b', 'c')

# 常见用途
# 1. 遍历两个列表对应元素
for num, letter in zip(a, b):
    print(num, letter)

# 2. 创建字典
keys = ['name', 'age', 'city']
values = ['Alice', 23, 'New York']
d = dict(zip(keys, values))
print(d) # {'name': 'Alice', 'age': 23, 'city': 'New York'}

# 字符串
s = "123456789"
print(s[:1]) # 1
print(s[1:]) # 23456789
# 字符串的计数
print(s[:1].count('1')) # 1
print(s[1:].count('1')) # 0

# 集合的使用
my_set = {'a', 'e', 'i', 'o', 'u'}

s = "abciiidef"
enumerate(s)  # 返回一个枚举对象，包含索引和值的元组
nums = [1, 12, -5, -6, 50, 3]
enumerate(nums)  # 返回一个枚举对象，包含索引和值的元组
print(list(enumerate(nums)))  # [(0, 1), (1, 12), (2, -5), (3, -6), (4, 50), (5, 3)]
print(nums[0:2]) # [1, 12]
print(nums[0:6]) # [1, 12, -5, -6, 50, 3]

n = [1,2,3,4,5,6,7,8,9,10]
print(sum(n[0:3])/3)

11 // 4 # 2 整除

blocks = "WBBWWBBWBW"
print(blocks.count('W')) # 5