# 个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

# 调用 个数可变的位置参数
fun(10, 20, 30, 40) # <class 'tuple'>元组类型
print('-' * 16)
fun(10)
print('-' * 16)
fun([10, 20, 30, 40]) # 传递的是一个参数，列表
# 在调用时，参数前加一颗星，将列表进行解包
fun(*[11, 22, 33, 44])

# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key, '-----', value)

# 调用
print('-' * 16)
fun2(name = 'Armin', age = 14, height = 166) # 关键字参数

d = {'name':'Armin', 'age':14, 'height':166}
# fun2(d)
fun2(**d)