class BaseClassNameA:
    def __init__(self, name):
        self.name = name
    
    def showA(self):
        print('基类A中的方法')

class BaseClassNameB:
    def __init__(self, age):
        self.age = age
    
    def showB(self):
        print('基类B中的方法')
# 多继承
class DerivedClassName(BaseClassNameA, BaseClassNameB):
    def __init__(self, name, age, gender):
        # 
        BaseClassNameA.__init__(self, name)
        BaseClassNameB.__init__(self, age)
        self.gender = gender


derived = DerivedClassName('312大人', 17, '女') 
derived.showA()
derived.showB()