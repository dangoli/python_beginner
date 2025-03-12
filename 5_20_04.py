class Car(object):
    def __init__(self, type, no):
        self.type = type
        self.no = no
    
    def run(self):
        print('我是车,我会跑')
    
    def stop(self):
        print('我是车,我会停')

# 出租车
class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company
    # 重写基类方法
    def run(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车,我的车牌号是:{self.no},您的目的地是？')
    
    def stop(self):
        print('目的地到了,您需付款,欢迎下次乘坐')

# 家用汽车
class FamilyCar(Car):
    def __init__(self, type, no, brand):
        super().__init__(type, no)
        self.brand = brand
    # 重写基类方法
    def run(self):
        print(f'我是:{self.brand}家用汽车,我的汽车我做主')
    
    def stop(self):
        print('目的地到了,下车')

# 
taxi = Taxi('tsl', '京A12345', '滴滴')
taxi.run()
taxi.stop()

print('-' * 20)
familycar = FamilyCar('小米汽车', '京B12345', '312大人')
familycar.run()
familycar.stop()