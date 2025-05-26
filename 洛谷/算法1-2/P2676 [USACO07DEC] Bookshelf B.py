# 排序一遍，从后往前取奶牛直到总和大于B

import sys
input = sys.stdin.readline

# N B
N, B = map(int, input().split())
a = list()

for i in range(N):
    a.append(int(input()))

a.sort(reverse = True)

# 便利a，从前到后计数
cnt = 0
s = 0 # 用于记录当然高度
for i in range(N):
    s += a[i]
    cnt += 1
    if s >= B:
        break
    

print(cnt)
# AC
