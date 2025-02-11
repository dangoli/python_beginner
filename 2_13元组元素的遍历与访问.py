t = ('python', 'hello', 'world')
# 根据索引访问元素
print(t[0]) # python

t2 = t[0:3:2] # 元组支持切片操作
print(t2) # ('python', 'world')

# 元组的遍历
for item in t:
    print(item)

# for + range()+ len()
for i in range(len(t)):
    print(i, t[i])

# enumerate()
for index, item in enumerate(t):
    print(index, '--->', item) # 可手动修改序号

for index, item in enumerate(t, start=11): # 序号从11开始
    print(index, '--->', item)