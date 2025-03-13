from datetime import datetime
from datetime import timedelta
# 创建两个datetime对象
dt1 = datetime(2017, 9, 1, 12, 30, 30)
dt2 = datetime(2020, 9, 1, 17, 30, 30)
print(dt2 - dt1) # 1096 days, 5:00:00

# 通过传参的方式创建timedelta对象
td1 = timedelta(10) # 10天
print(td1) # 10 days, 0:00:00
td2 = timedelta(10, 11) # 10天11秒
print(td2) # 10 days, 0:00:11