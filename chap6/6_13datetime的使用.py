from datetime import datetime
dt = datetime.now() # 获取当前时间
print('当前的系统时间:', dt)

# datetime是一个类，可以通过类方法获取时间
dt2 = datetime(2025, 8, 1, 12, 30, 30) # 获取指定时间
print('dt2的数据类型:', type(dt2))
print('dt2指定的时间:', dt2)
print('年:', dt2.year)
print('月:', dt2.month)
print('日:', dt2.day)
print('时:', dt2.hour)
print('分:', dt2.minute)
print('秒:', dt2.second)

# 比较两个时间的大小
print('dt2是否大于dt:', dt2 > dt)

# datetime对象转换为字符串
dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
print('dt转换为字符串:', dt_str)
print('dt的数据类型:', type(dt))
print('dt_str的数据类型:', type(dt_str))

# 字符串转换为datetime对象
str_dt = '2025-06-01 12:30:30'
dt3 = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
print('str_dt转换为datetime对象:', dt3)
print('dt3的数据类型:', type(dt3))