def takeFirst(ele): # 二维列表排序函数
    return ele[0]

n = int(input())
record = []
# rec = [0, 0]
for i in range(n):
    a = input()
    rec = [int(j) for j in a.split()] # 接收输入的两数字，以空格隔开
    record.append(rec)

if n == 1: # 防止j的溢出
    record_merge = record
else:
    rec = [0, 0]
    record_merge = [] # 新建列表存储合并后的二维列表
    found = [] # 记录已经查找过的索引值
    for i in range(len(record)):
        a = record[i][0]
        b = record[i][1]
        while a not in found:
            rec[0] = a
            rec[1] = b # 写在这里，如果索引只出现一次也。。
            for j in range(i+1, len(record)): # 开始查找
                if record[j][0] == a:
                    rec[1] = rec[1] + record[j][1]
            found.append(a) # 更新查找过的索引值
            temp_rec = rec[:] # 防止变量rec更新覆盖
            record_merge.append(temp_rec)

record_merge.sort(key=takeFirst)
for item in record_merge:
    for i in item:
        print(i, end=' ')
    print()