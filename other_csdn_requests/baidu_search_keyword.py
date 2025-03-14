import requests
keyword = 'Python'
try: # 尝试执行下面的代码
    kv = {'wd' : keyword} # 构造字典 注意这里的键wd是百度搜索的关键字
    r = requests.get('http://www.baidu.com/s', params=kv) # 发送请求
    print(r.request.url) # 打印url
    r.raise_for_status() # 如果状态不是200，引发HTTPError异常
    print(len(r.text)) # 打印网页内容长度
except: # 如果有异常发生就执行下面的代码
    print('爬取失败') # 打印爬取失败