def special_IP(str1): # 函数返回值为bool类型
    """
    判断是否是特殊IP
    """
    flag_special = False # 标志位, 默认不是特殊IP
    a, b, c, d = str1.split(".")
    a = int(a)
    if a == 0 or a == 127:
        flag_special = True
        return flag_special
    else:
        return flag_special

def is_IP(str1): # 函数返回值为bool类型
    """
    判断是否是正确的IP
    """
    flag_IP = False # 标志位, 默认不是正确IP
    a, b, c, d = str1.split(".")
    if a == "" or b == "" or c == "" or d == "":
        return flag_IP # 有空段, 不是正确IP
    else:
        flag_IP = True # 是正确IP
    return flag_IP

def is_subnet(str2): # 函数返回值为bool类型
    """
    判断是否是正确的子网掩码
    全为1的掩码也视为非法
    全为0的掩码也视为非法
    """
    flag_subnet = False # 标志位, 默认不是正确子网掩码
    bin_str = ""
    a, b, c, d = str2.split(".")
    for item in [a, b, c, d]:
        if item == "":
            return flag_subnet # 有空段, 不是正确子网掩码
        num = int(item)
        bin_item = bin(num)[2:] # 转为二进制字符串
        bin_item = "0" * (8 - len(bin_item)) + bin_item # 补齐8位
        bin_str += bin_item
    if "01" in bin_str: # 出现了0后面又出现1的情况, 不是正确子网掩码
        return flag_subnet
    if bin_str == "11111111111111111111111111111111": # 全为1的掩码, 不是正确子网掩码
        return flag_subnet
    if bin_str == "00000000000000000000000000000000": # 全为0的掩码, 不是正确子网掩码
        return flag_subnet
    flag_subnet = True # 是正确子网掩码
    return flag_subnet

def count_type(str1): # 计算IP类型, 前提是str1是正确的IP
    """
    A类: 0.0.0.0 - 127.255.255.255
    B类: 128.0.0.0 - 191.255.255.255
    C类: 192.0.0.0 - 223.255.255.255
    D类: 224.0.0.0 - 239.255.255.255
    E类: 240.0.0.0 - 255.255.255.255
    """
    a, b, c, d = str1.split(".")
    a = int(a)
    n_a, n_b, n_c, n_d, n_e = 0, 0, 0, 0, 0
    if 1 <= a <= 127:
        n_a += 1
    elif 128 <= a <= 191:
        n_b += 1
    elif 192 <= a <= 223:
        n_c += 1
    elif 224 <= a <= 239:
        n_d += 1
    elif 240 <= a <= 255:
        n_e += 1
    return n_a, n_b, n_c, n_d, n_e

def count_private(str1): # 计算私有IP个数, 前提是str1是正确的IP
    """
    私有IP范围:
    "10.0.0.0" - "10.255.255.255"
    "172.16.0.0" - "172.31.255.255"
    "192.168.0.0" - "192.168.255.255"
    """
    n_private = 0
    a, b, c, d = str1.split(".")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if a == 10:
        n_private += 1
    elif a == 172 and 16 <= b <= 31:
        n_private += 1
    elif a == 192 and b == 168:
        n_private += 1
    return n_private

n_a, n_b, n_c, n_d, n_e, n_err, n_private = 0, 0, 0, 0, 0, 0, 0
while True:
    try:
        line = input().strip()
        if not line:   # 用户只按回车
            break
        str1, str2 = line.split("~")
        if special_IP(str1): # 是特殊IP的话就是True, 直接跳过
            continue

        # 不是特殊IP的话, 判断是否是正确的IP和正确的子网掩码, 每行输入只算一次错误
        if not is_IP(str1) or not is_subnet(str2): # 如果不是正确的IP, n_err += 1
            n_err += 1
            continue

        else: # 是正确的IP, 计算类型和私有IP
            n1, n2, n3, n4, n5 = count_type(str1)
            n_a += n1
            n_b += n2
            n_c += n3
            n_d += n4
            n_e += n5
            n_private += count_private(str1)
    except EOFError:  # 输入结束 (Ctrl+D 或 Ctrl+Z)
        break

print(n_a, n_b, n_c, n_d, n_e, n_err, n_private)

""""
10.70.44.68~1.1.1.5
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
"""