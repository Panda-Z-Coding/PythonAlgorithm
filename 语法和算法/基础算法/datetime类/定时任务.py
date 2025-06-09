import os
import sys
input = sys.stdin.readline
import datetime
# 用控制语句，先查看当前字符串有没有 , - *

# 2023 年总共会执行几次

# 2023 月份 {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
# print(2023 % 400 == 0 or (2023 % 4 == 0 and 2023 % 100 != 0)) # False

# print(3 * (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31)) # 1095 计算正确

# 那就是按照这个算法来

# 我们先要解析字符串

time = input().split()
a = [[0, 59], [0, 59], [0, 23], [1, 31], [1, 12]] # 每一个值的范围

# 解析每一个参数对应的范围
for i in range(5):
    if '*' in time[i]:
        time[i] = range(a[i][0], a[i][1] + 1)
    elif '-' in time[i]:
        l, r = map(int, time[i].split('-'))
        time[i] = range(l, r + 1)
    elif ',' in time[i]:
        time[i] = list(map(int, time[i].split(',')))
    else:
        time[i] = [int(time[i])]

s, f, h, d, m = time

days = len(s) * len(f) * len(h) # 这是一天要执行的
# 之后检查每一天，如果在范围内就加上days

start = datetime.date(2023, 1, 1)
end = datetime.date(2024, 1, 1)
t = datetime.timedelta(days = 1)
cnt = 0
while start < end:
    _, M, D = map(int, str(start).split('-'))

    if M in m and D in d:
        cnt += days
    
    start += t

print(cnt)








