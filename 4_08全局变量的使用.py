a = 100 # 全局变量

def calc(x, y):
    return a + x + y
print(a) # 100
print(calc(10, 20)) # 120
print('-' * 16)

def calc2(x, y):
    a = 200 # 局部变量的名称和全局变量名称相同
    return a + x + y

print(a) # 100
print(calc2(10, 20)) # 230

def calc3(x, y):
    global s # 使用global关键字声明，是全局变量
    s = 300 # 声明和定义分开执行
    return s + x + y

print(calc3(10, 20)) # 330
print(s) # 300