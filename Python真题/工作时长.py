import os
import sys
# 又是一个时间类的模拟, 还需要排序一下, 用字符串转化成datetime
from datetime import *

ti = [input().strip() for i in range(520)]

ti = sorted(ti)
# print(*ti, sep = '\n')
ssum = 0
for i in range(0, 520, 2):
    # 每次选出i和i-1
    # print(i)
    c1 = datetime.strptime(ti[i], '%Y-%m-%d %H:%M:%S')
    c2 = datetime.strptime(ti[i + 1], '%Y-%m-%d %H:%M:%S')
    t = c2 - c1
    ssum += int(t.total_seconds())
print(ssum)
    




