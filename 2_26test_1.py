lst = [88, 89, 90, 98, 00, 99]
print(lst) # [88, 89, 90, 98, 0, 99]
# 遍历列表的方式
# for index in range(len(lst)):
#     if str(lst[index]) != '0':
#         lst[index] = '19' + str(lst[index]) # 拼接年份，再赋值
#     else:
#         lst[index] = '200' + str(lst[index])

# print('修改之后的年份：', lst) # 修改之后的年份： ['1988', '1989', '1990', '1998', '2000', '1999']

# 使用enumerate()函数
for index, value in enumerate(lst):
    if str(lst[index]) != '0':
         lst[index] = '19' + str(value) # 拼接年份，再赋值
    else:
         lst[index] = '200' + str(value)
print('修改之后的年份：', lst)