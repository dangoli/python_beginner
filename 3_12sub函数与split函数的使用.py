import re
pattern = '黑客|破解|反爬'
s = '我想学习python，想破解一些VIP视频，python可以实现无底线反爬吗？'
new_s = re.sub(pattern, 'XX', s)
print(new_s) # 我想学习python，想XX一些VIP视频，python可以实现无底线XX吗？

s2 = 'https://www.bing.com/search?q=leehan&qs=n'
pattern2 = '[?|&]' # 模式字符串
lst = re.split(pattern2, s2)
print(lst) # ['https://www.bing.com/search', 'q=leehan', 'qs=n']
