class Person():
    def eat(self):
        print('人，吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗，爱吃骨头')
        
# 三个类中都有同名的方法，这就是多态
# 编写一个调用函数
def fun(obj):
    obj.eat()

# 创建三个类的对象
per = Person()
cat = Cat()
dog = Dog()

# 调用fun()函数
fun(per) # python中的多态,不关心对象的类型，只关心对象是否具有同名方法
fun(cat)
fun(dog)