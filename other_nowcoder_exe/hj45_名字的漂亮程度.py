"""
对于给定的由小写字母组成的字符串，定义字符串的"漂亮度"为: 该字符串中所有字母"漂亮度"的总和.
每一个字母的"漂亮度"由你来确定, 具体规则如下:
1. 每一个字母的"漂亮度"是一个介于1到26之间的整数.
2. 没有两个字母的"漂亮度"是相同的.
现在, 你需要确定每个字母的"漂亮度", 以使得该字符串的"漂亮度"最大.
输入描述:
输入包含多组测试数据. 第一行输入一个整数T(1 ≤ T ≤ 10), 表示测试数据的组数, 每组测试数据描述如下:
在一行中输入一个仅包含小写字母的字符串s, 字符串长度不超过10000.
输出描述:
对于每组测试数据, 输出一个整数, 表示该字符串最大的"漂亮度".
"""

def beauty_score():
    s = input().strip()
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    freq.sort(reverse=True)
    sum = 0
    beauty = 26
    for f in freq:
        if f == 0:
            break
        sum += f * beauty
        beauty -= 1
    return sum

while True:
    try:
        T = int(input())
        res = [0] * T
        for i in range(T):
            res[i] = beauty_score()
        for r in res:
            print(r)

    except EOFError:
        break