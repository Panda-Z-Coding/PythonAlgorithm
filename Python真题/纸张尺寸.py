import os
import sys

s = input()
idx = int(s[1])

ans = [[1189, 841]]
for i in range(1, 9 + 1):
    l, w = ans[i-1][0], ans[i-1][1]
    # 先获取前一个的长宽
    # 然后比较长//2
    l = l // 2
    ans.append([w, l])
print(*ans[idx], sep = '\n')
