def happy_birthday(name, age):
    print('祝' + name + '生日快乐！')
    print(str(age) + '岁生日快乐！')

# 调用
# happy_birthday('LEEHAN') # TypeError: happy_birthday() missing 1 required positional argument: 'age'
happy_birthday('Armin', 14)
