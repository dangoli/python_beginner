import time # 引入time模块
now = time.time() # 获取当前时间
print(now) # 输出当前时间

obj = time.localtime() # 获取当前时间的时间元组
print(obj) # 输出当前时间的时间元组 

obj2 = time.localtime(60) # 获取60秒之后的时间元组
print(obj2) # 输出60秒之后的时间元组
print(type(obj2)) # <class 'time.struct_time'>
print('年份:', obj2.tm_year) # 年份: 1970
print('月份:', obj2.tm_mon) # 月份: 1   
print('日期:', obj2.tm_mday) # 日期: 1
print('小时:', obj2.tm_hour) # 小时: 0
print('分钟:', obj2.tm_min) # 分钟: 1
print('秒:', obj2.tm_sec) # 秒: 0
print('星期:', obj2.tm_wday) # 星期: 3
print('一年中的第几天:', obj2.tm_yday) # 一年中的第几天: 1
print('是否为夏令时:', obj2.tm_isdst) # 是否为夏令时: -1

print(time.ctime()) # 输出当前时间的字符串格式

# 格式化时间
print(time.strftime('%Y-%m-%d', time.localtime())) # 
print(time.strftime('%H:%M:%S', time.localtime())) #
print(time.strftime('%B %d %A %Y %I:%M:%S %p', time.localtime())) # 月份 日期 星期 年份 小时:分钟:秒 上午/下午

# 将时间字符串转换为时间元组
print(time.strptime('2025-06-01', '%Y-%m-%d')) # 将时间字符串转换为时间元组

time.sleep(2) # 程序休眠2秒