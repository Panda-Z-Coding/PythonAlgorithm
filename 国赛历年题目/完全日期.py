import os
import sys

'''
这里我们来复习一下datetime这个类
'''
import datetime

s_date = datetime.date(2001, 1, 1)
d_date = datetime.timedelta(days = 1)
e_date = datetime.date(2021, 12, 31)

d = 0 # 用于记录数字和
c = 0

while s_date != e_date:
    da = datetime.datetime.strftime(s_date, "%Y%m%d")
    for i in da:
        d += int(i)
    e = d ** 0.5
    if e % 1 == 0: #!  很好的判断一个数字是否是完全平方的方法
        c += 1
    d = 0
    s_date += d_date
print(c)