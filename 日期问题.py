# import os
# import sys

# 请在此输入您的代码
# a = list(input().split('/'))
# 1960 年 1 月 1 日至 2059 年 12 月 31 日
# 年/月/日  月/日/年  日/月/年
# 中间不可能是年
# a[0] -> 年、月、日
# a[1] -> 月、日
# a[2] -> 日、年

# 把所有组合都求出来然后判断那些在这个区间
# 年 -> a[0]、a[2] -> if >= 60: +19 else: +20
# 月 -> a[0]、a[1]
# 日 -> a[0]、a[1]、a[2]

# year = []

# for y in [a[0], a[2]]:
#     for m in [a[0], a[1]]:
#         for d in [a[0], a[1], a[2]]:
#             s = '-'
#             if int(y) >= 60 and int(m) <= 12 and int(d) <= 31 and int(y) != int(m) and int(y) != int(d) and int(m) != int(d):
#                 s = '19' + str(y) + s + str(m) + s + str(d)
#             if int(y) < 60 and int(m) <= 12 and int(d) <= 31 and int(y) != int(m) and int(y) != int(d) and int(m) != int(d):
#                 s = '20' + str(y) + s + str(m) + s + str(d)
#             year.append(s)

# for i in year:
#     if i != '-':
#         print(i)
        
import os
import sys
from datetime import date
# 请在此输入您的代码
info = input().split('/')
aa = int(info[0])
bb = int(info[1])
cc = int(info[2])
d = set()

def Year(y):
  return (1900 + y if y >= 60 else 2000 + y)
def D(a, b, c):
  try:
    day = date(Year(a), b, c)
    d.add(str(day))
  except:
    pass

D(aa,bb,cc)
D(cc,aa,bb)
D(cc,bb,aa)

d = list(d)
d.sort()
for j in d:
  print(j)