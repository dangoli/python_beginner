"""
对于给定的分类规则集R={R1,R2,...,Rm}, 规范化它, 具体地:将R中的整数按照从小到大的顺序重新排序; 去除R中的重复元素.
记规范化后的分类规则集为r={r1,r2,...,rk}, 其中k<=m, 且r1<r2<...<rk.
对于给定的整数集合I={I1,I2,...,In}, 按照下方要求, 使用规范化后的分类规则集r输出分类后的结果. 
对于第i条分类规则ri, 如果I中存在以ri为连续子串的整数, 则该规则集有效, 进一步地, 你需要输出有多少条数据符合该规则, 以及这些数据在I中的位置, 数据本身.
(本题中需要将整数看成数字字符串)
输入描述:
第一行先输入一个整数n(1到100)代表数据集I中的数据条数, 随后, 在同一行输入n个整数I1,I2,...,In, 这些整数两两之间用空格隔开.
第二行先输入一个整数m(1到100)代表分类规则集R中的规则条数, 随后, 在同一行输入m个整数R1,R2,...,Rm, 这些整数两两之间用空格隔开.
输出描述:
在一行上:
先输出一个整数k, 代表一共要输出的数字个数.
随后, 对于规范后的每一条规则, 如果有效, 先输出该规则, 再输出一个整数p, 代表符合该规则的数据条数, 随后输出p个二元数组, 代表符合该规则的数据在I中的位置与数据本身. 其中位置从0开始计数.
如果其无效, 则跳过该规则
"""

i = input().strip()
r = input().strip()
i_list = i.split()[1:] # 数据集I
r_list = sorted(set(r.split()[1:]), key=int) # 规范化分类规则集R
result = [] # 最终结果
for rule in r_list:
    temp = []
    for index, num in enumerate(i_list):
        if rule in num:
            temp.append((index, num))
    if temp:
        result.append((rule, len(temp), temp))
if result:
    n_rules = len(result)
    counts_sum = sum(item[1] for item in result)   # 所有有效规则的匹配总数
    s = 2 * (n_rules + counts_sum)
    print(s, end=' ')
    for res in result:
        print(res[0], res[1], end=' ')
        for t in res[2]:
            print(t[0], t[1], end=' ')