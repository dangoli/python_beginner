# 创建字典用于存储车票信息，使用车次作key，使用其他信息作value
dict_ticket = {
    'G1569':['北京南-天津南', '18:06', '18:39', '00:33'],
    'G1567':['北京南-天津南', '18:15', '18:49', '00:34'],
    'G8917':['北京南-天津南', '18:20', '19:19', '00:59'],
    'G9551':['北京南-天津南', '18:35', '19:09', '00:34']
}
print('车次     出发站-到达站       出发时间        到达时间        历时时长')
# 遍历字典中的元素
for key in dict_ticket.keys():
    print(key, end=' \t')
    for item in dict_ticket.get(key):
        print(item, end=' \t\t')
    print()