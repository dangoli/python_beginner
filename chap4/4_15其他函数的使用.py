# format()
print(format(3.14, '20')) # 数值型默认右对齐
print(format('hello', '20')) # 字符串型默认左对齐
print(format('hello', '*<20')) # <左对齐，*表示填充符，20表示显示宽度
print(format('hello', '*>20'))
print(format('hello', '*^20'))  


print(format(3.141592653, '.2f'))
print(format(20, 'b')) #二进制
print(format(20, 'o')) #八进制
print(format(20, 'x')) #十六进制
print(format(20, 'X')) #十六进制

print('-' * 16)
print(len('helloworld'))
print(len([1,2,3,4,5]))

print('-' * 16)
print(id(10))
print(id('helloworld'))
print(type('hello'), type(10))

print(eval('1+3'))
print(eval('1>3'))