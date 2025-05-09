class Person: # 默认继承了object
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我是：{self.name}, 我今年：{self.age}岁')
        
# Student继承person类
class Student(Person):
    # 编写初始化的方法
    def __init__(self, name, age, stuno):
        super().__init__(name, age) # 调用基类的初始化方法
        self.stuno = stuno
    
    def show(self):
        super().show()
        print(f'我就读于SEU，我的学号是：{self.stuno}')

# Doctor继承Person类
class Doctor(Person):
    # 
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    
    def show(self):
        # return super().show()
        print(f'我是：{self.name}, 我今年{self.age}岁, 我工作科室是：{self.department}')



# 创建第一个子类对象
stu = Student('312大人', 22, '1001')
stu.show()

doctor = Doctor('LEEHAN', 28, '儿科')
doctor.show()