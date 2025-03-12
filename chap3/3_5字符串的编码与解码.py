s = '中国梦梦之蓝'
# 编码 str->bytes
scode = s.encode(errors='replace') # 默认是UTF-8，中文占3个字节
print(scode)

scode_gbk = s.encode('gbk', errors='replace') # gbk中文占2个字节
print(scode_gbk)

# 编码中的出错问题
s2 = '耶✌'
scode_error = s2.encode('gbk', errors='replace')
print(scode_error)

# 解码过程 bytes-> str
print(bytes.decode(scode_gbk, 'gbk')) # 中国梦梦之蓝
print(bytes.decode(scode, 'utf-8'))