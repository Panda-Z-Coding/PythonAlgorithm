import os
import sys
# input = sys.stdin.readline
# 互不重叠
# 子串! 一定连续
# 贪心的思路来看的话, 是不是在?的地方填入前面一个数字

s = input()
n = len(s) 
s = '?' + s
# 先遍历一遍, 把所有的? 变成前面一个

f = [0] * (n + 1)
for  i in range(2, n + 1):
    if s[i - 1] == '?' or s[i] == '?' or (s[i] == s[i - 1]):
        f[i] = f[i - 2] + 1
    else:
        f[i] = f[i - 1]

# print(s)
print(f[n])

