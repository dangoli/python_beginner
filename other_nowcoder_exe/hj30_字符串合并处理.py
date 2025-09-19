"""
对于给定的由大小写字母和数字构成的字符串s和t, 记下标从1开始. 按以下两个阶段进行处理:
合并阶段:
第一步: 将s和t合并, 形成一个新字符串u.
第二步: 将u中奇数位字符按ASCII码从小到大排序, 随后偶数位字符也按ASCII码从小到大排序, 得到u'.
调整阶段:
随后, 从左到右遍历u'中的每一个字符
第一步, 如果该字符不是合法十六进制字符(0-9, a-f, A-F), 则不做任何处理. 直接追加到结果中; 否则, 将其转换为十进制数.
第二步, 将该十进制数转换为4位二进制数, 例如, 0转换为0000, 7转换为0111, 10转换为1010, 15转换为1111.
第三步, 将该二进制数的高低位进行交换, 例如, 0111转换为1110, 1010转换为0101.
第四步, 将该二进制数转换为大写的十六进制数, 追加到结果中.
最终输出上述拼接而成的字符串.
输入描述:
在一行上输入两个长度在1到100之间的由大小写字母和数字构成的字符串s和t, 以空格隔开.
输出描述:
输出经过处理后的最终字符串.
"""

def process_str():
    s, t = input().split()
    u = s + t
    u_odd = sorted(u[::2])
    u_even = sorted(u[1::2])
    u_prime = []
    for i in range(len(u)):
        if i % 2 == 0:
            u_prime.append(u_odd[i // 2])
        else:
            u_prime.append(u_even[i // 2])
    # 十六进制合法字符集合
    hex_set = set('0123456789abcdefABCDEF')
    res = []
    for ch in u_prime:
        if ch not in hex_set:
            res.append(ch)
        else:
            dec_value = int(ch, 16) # 十六进制转换为十进制
            bin_value = f"{dec_value:04b}" # 十进制转换为4位二进制
            swapped = bin_value[::-1] # 高低位交换
            res.append(format(int(swapped, 2), "X")) # 二进制转换为大写十六进制
    print("".join(res))

if __name__ == "__main__":
    process_str()