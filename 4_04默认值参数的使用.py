def happy_birthday(name = 'Armin', age = 14):
    print('祝' + name + '生日快乐！')
    print(str(age) + '岁生日快乐！')

# 调用
happy_birthday()
happy_birthday('Mikasa') # 位置传参
happy_birthday(age=19) # 关键字传参，name采用默认值

# def asisi(a=10, b):
#     pass
def asisi(a, b=10): 
    pass