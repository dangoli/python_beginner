# class MyClass(object):
#     def __init__(self, name, age):
#         print('name:', name, 'age:', age)

# obj = MyClass('312大人', 20)

# class Person(object):
#     def __init__(self, xm, nl):
#         self.name = xm
#         self.age = nl

#     def show():
#         print(f'{self.name}说:我{self.age}岁')

# per = Person('312大人', 20)
# per.show()

# class BaseClassName:
#     a = 'hello'
#     def show(self):
#         print('BaseClass')

# class DerivedClassName(BaseClassName):
#     pass

# d = DerivedClassName()
# print(d.a) # hello
# d.show() # BaseClass

class A:
    def show(self):
        print(1)

class B:
    def show(self):
        print(2)

class C(A, B):
    def show(self): # 重写基类的方法
        print(3)

c = C()
c.show() # 3