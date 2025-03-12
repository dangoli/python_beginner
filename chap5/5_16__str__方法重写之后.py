class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 方法重写
    def __str__(self):
        return '这是一个人类，具有name和age两个属性' # 返回值是一个字符串

# 创建person对象
per = Person('312大人', 20)
print(per) 
print(per.__str__()) # 调用__str__()方法