import requests
url = 'https://www.python.org/dev/peps/pep-0020/'
res = requests.get(url) # 发送请求
text = res.text # 获取网页内容
text # 打印网页内容
with open('zen_of_python.txt', 'w') as f: # 以写入模式打开文件
    f.write(text[text.find('<pre>')+28:text.find('</pre>')-1]) # 写入文件
print(text[text.find('<pre>')+28:text.find('</pre>')-1]) # 打印文本内容