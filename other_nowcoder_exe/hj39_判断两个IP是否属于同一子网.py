def is_subnet(str_sub):
    """
    判断是否是正确的子网掩码, 加入负数值的判断
    """
    flag_sub = False # 标志位，默认不是正确的子网掩码
    bin_str =""
    a, b, c, d = str_sub.split(".")
    for item in [a, b, c, d]:
        if item == "":
            return flag_sub # 有空段，不是正确的子网掩码
        num = int(item)
        if num < 0 or num > 255:
            return flag_sub
        bin_item = bin(num)[2:] # 转为二进制字符串
        bin_item = "0" * (8 - len(bin_item)) + bin_item # 补齐8位
        bin_str += bin_item
    if "01" in bin_str: # 出现了0后面又有1的情况, 不是正确的子网掩码
        return flag_sub 
    if bin_str == "11111111111111111111111111111111":
        return flag_sub
    if bin_str == "00000000000000000000000000000000":
        return flag_sub
    flag_sub = True
    return flag_sub

def is_IP(str_ip):
    """
    判断是否是正确的IP地址
    """
    flag_IP = False # 标志位, 默认不是正确的IP 
    a, b, c, d = str_ip.split(".")
    if a == "" or b == "" or c == "" or d == "":
        return flag_IP
    else:
        a_i, b_i, c_i, d_i = int(a), int(b), int(c), int(d)
        if a_i < 0 or a_i > 255 or b_i < 0 or b_i > 255 or c_i < 0 or c_i > 255 or d_i < 0 or d_i > 255:
            return flag_IP
        else:
            flag_IP = True
    return flag_IP

def trans_ip(str1):
    bin_str = ""
    a_ip, b_ip, c_ip, d_ip = str1.split(".")
    for item in [a_ip, b_ip, c_ip, d_ip]:
        num = int(item)
        bin_item = f"{num:08b}" # 直接转成8位二进制
        bin_str += bin_item
    return bin_str

def judge():
    flag_s = False # 标志位, 默认属于不同子网络
    sub_ip = input()
    ip1 = input()
    ip2 = input() # 只处理3行的版本
    flag_sub = is_subnet(sub_ip) # 判断子网掩码格式正确与否, 如果不正确就是False
    flag_ip1 = is_IP(ip1)
    flag_ip2 = is_IP(ip2) 
    # 先检查合法性再调用trans_ip
    if not (flag_ip1 and flag_ip2 and flag_sub):
        print(1)
        return
    
    bin_ip1 = trans_ip(ip1) # ip1的二进制字符串
    bin_ip2 = trans_ip(ip2) # ip2的二进制字符串
    bin_sub = trans_ip(sub_ip)
    int_ip1 = int(bin_ip1, 2) # 转成整数, &运算符只能用于整数类型和bool类型
    int_ip2 = int(bin_ip2, 2)
    int_sub = int(bin_sub, 2)
    res1 = int_ip1 & int_sub #是Int类型 
    res2 = int_ip2 & int_sub #
    if res1 == res2:
        print(0)
    else:
        print(2)

if __name__ == "__main__":
    judge()