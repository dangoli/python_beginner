# 统计字符串中出现指定字符的次数
s = 'HelloPython,HelloJava,hellophp'
letter = input('请输入要统计的字符：')
LETTER = letter.upper()
print('{0}在{1}中一共出现了{2}次'.format(letter, s, s.upper().count(LETTER)))