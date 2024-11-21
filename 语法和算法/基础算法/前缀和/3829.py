import os
import sys

# 请在此输入您的代码
'''
费用: 重量 * 移动距离
目标: 全都移动到同一位置

A从1移到5和1 - 3 - 5花费是一样的！
'''

n = int(input())
s = []
for _ in range(n):
    w, p = map(int, input().split())
    s.append([w, p])
s.sort(key=lambda x: x[1])

pre = [0] * n
sub = [0] * n

acc1 = s[0][0]
acc2 = s[-1][0]

for i in range(1, n):
    pre[i] = pre[i-1] + acc1 * (s[i][1] - s[i-1][1])
    acc1 += s[i][0]

for i in range(n-2, -1, -1):
    sub[i] = sub[i+1] + acc2 * (s[i+1][1] - s[i][1])
    acc2 += s[i][0]

cost = min([pre[i] + sub[i] for i in range(n)])
print(cost)