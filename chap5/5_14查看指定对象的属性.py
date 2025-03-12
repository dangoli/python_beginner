class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我是：{self.name}，今年{self.age}岁了')

# 创建一个Person类的对象
per = Person('312大人', 20)
print(dir(per)) # 查看对象的所有属性和方法

print(per) # 自动调用了__str__()方法