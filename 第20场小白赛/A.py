import os
import sys
import math
# 请在此输入您的代码

n, m, k = map(int, input().split())
#茶杯数量、茶壶容量、装满的数量
tee_cup = list(map(int, input().split()))

tee_cup.sort()
tee_m = 0
tee_yu = 0 #余下的水
ans = 0
for i in range(n):
    # current_cup = tee_cup[i]
    
    while tee_cup[i] > 0:
        tee_yu = abs(tee_cup[i] - m)
        tee_cup[i] -= m
        ans += 1
    if tee_cup[i] < 0:
        tee_m += 1
    if tee_m == k:
        break

    tee_cup[i+1] -= tee_yu
        
print(ans)    