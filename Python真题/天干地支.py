
##print(2020 % 60)
##print(1960 % 60)
##print(1900 % 60)
##print(2019 % 60)

# 先模拟出第一轮60个年份
# nian = [] # 下标从0开始
# 2020是庚子年 -> 2032是壬子年 -> 2044是甲子年 -> 2044%60 = 4
tian = ['jia', 'yi', 'bing', 'ding', 'wu', 'ji', 'geng', 'xin', 'ren', 'gui']
di = [
    'zi',
    'chou',
    'yin',
    'mao',
    'chen',
    'si',
    'wu',
    'wei',
    'shen',
    'you',
    'xu',
    'hai'
]
n = int(input())
c = n - 4
a = c % 10
b = c % 12
print(tian[a] + di[b])





