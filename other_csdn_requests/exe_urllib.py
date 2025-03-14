import urllib
import urllib.request
import requests
url = 'https://peps.python.org/pep-0020/' 
res = urllib.request.urlopen(url).read().decode('utf-8') # 发送请求
print(res[res.find('<pre>')+28:res.find('</pre>')-1]) # 打印网页内容
