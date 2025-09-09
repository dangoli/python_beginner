def int_to_ip(int32):
    return '.'.join([str((int32 >> (8 * i)) & 0xFF) for i in range(4)[::-1]])

def ip_to_int(ip):
    parts = list(map(int, ip.split('.')))
    s_bin = ''.join([bin(p)[2:].zfill(8) for p in parts])
    return int(s_bin, 2)

s = input().strip()
if s.isdigit():
    print(int_to_ip(int(s)))
else:
    print(ip_to_int(s))