class Student():
    #
    def __init__(self, name, age, gender):
        self._name = name # self._name 表示受保护的，只有本类和子类可访问
        self.__age = age # self.__age 表示私有的， 只能类本身可去访问
        self.gender = gender # self.gender 表示普通的实例属性，类的内部外部、子类都可以访问
    
    def _fun1(self): # 受保护的
        print('子类及本身可访问')
    
    def __fun2(self): # 私有的
        print('只有定义的类可以访问')

    def show(self): # 
        self._fun1() # 类本身访问受保护的方法
        self.__fun2() # 类本身访问私有的方法
        print(self._name) # 受保护的实例属性
        print(self.__age) # 私有的实例属性

# 创建一个学生类的对象
stu = Student('312大人', 22, 'female')
# 类的外部
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?

# 调用受保护的实例方法
stu._fun1() # 子类及本身可以被访问
# stu.__fun2() # 私有方法 AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?


#
print(stu._Student__age)
stu._Student__fun2()

print(dir(stu))