# isdigit只识别十进制阿拉伯数字
print('123'.isdigit()) # True
print('一二三'.isdigit()) # False
print('0b1010'.isdigit()) # False
print('Ⅰ'.isdigit()) # 只识别十进制阿拉伯数字
print('-' * 32)
# 所有字符都是数字 
print('123'.isnumeric()) # True
print('一二三'.isnumeric()) # True
print('0b1010'.isnumeric()) # False
print('Ⅰ'.isnumeric()) # True 罗马数字
print('壹贰叁'.isnumeric()) # True
print('-' * 32)
# 所有字符都是字母 包括中文字符
print('hello世界'.isalpha()) # True
print('hello你好123'.isalpha()) # False
print('hello世界一二三'.isalpha()) # True
print('hello世界ⅠⅡ'.isalpha()) # False
print('-' * 32)

# 所有字符都是数字或字母
print('hello世界'.isalnum()) # True
print('hello你好123'.isalnum()) # True
print('hello世界一二三'.isalnum()) # True
print('hello世界ⅠⅡ'.isalnum()) # True


print('-' * 32)
# 判断字符的大小写
print('HelloWorld'.islower()) # False
print('helloworld'.islower()) # True
print('hello未来'.islower()) # True

print('-' * 32)
print('HelloWorld'.isupper()) # False
print('HELLOWORLD'.isupper()) # True
print('HELLO未来'.isupper()) # True
print('-' * 32)
#所有字符都是首字母大写
print('Hello'.istitle()) # True
print('HelloWorld'.istitle()) # False 因为非首字母也大写了
print('Helloworld'.istitle()) # True
print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False

# 判断是否都是空白字符
print('-' * 32)
print('\t'.isspace()) # True
print(' '.isspace()) # True
print('\n'.isspace()) # True