class Circle:
    def __init__(self, r):
        self.r = r

    def area(self): # 计算圆的面积
        return 3.14 * self.r * self.r

    def perimeter(self): # 计算圆的周长
        return 2 * 3.14 * self.r

# 创建一个圆对象
r = eval(input('请输入圆的半径:'))
c = Circle(r)
# 输出圆的面积和周长
area = c.area()
perimeter = c.perimeter()
print('圆的面积:', area)
print('圆的周长:', perimeter)