class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建类的对象
a = A()
b = B()
# 创建类C的对象
c = C('312大人', 20)

print('对象a的属性字典:', a.__dict__)
print('对象b的属性字典:', b.__dict__)
print('对象c的属性字典:', c.__dict__)

print('对象a所属的类:', a.__class__)
print('对象b所属的类:', b.__class__)
print('对象c所属的类:', c.__class__)

print('类A的基类元组:', A.__bases__)
print('类B的基类元组:', B.__bases__)
print('类C的基类元组:', C.__bases__)

print('类A的基类:', A.__base__)
print('类B的基类:', B.__base__)
print('类C的基类:', C.__base__) # 如果继承了多个基类，只会返回第一个基类

print('类A的层次结构:', A.__mro__)
print('类B的层次结构:', B.__mro__)
print('类C的层次结构:', C.__mro__)  # 类C的层次结构是C -> A -> B -> object

# 派生类列表
print('类A的派生类列表:', A.__subclasses__())
print('类B的派生类列表:', B.__subclasses__())
print('类C的派生类列表:', C.__subclasses__())