'''
import os
import sys

# 只要看和被指定的号码相距的距离

# 获取当前位置的下标，然后遍历一遍数组去更新当前位置的最大值

n, m = map(int, input().split())
a = list(map(int, input().split()))
score = [i for i in range(n + 1)] # 下标从1开始有效, 一开始 [0 , 1, 2, 3, 4, ... , n]
# print(score)
for j in range(1, n + 1):
    score[j] = abs(j - a[0])

for i in a[1:]:
    # 指定i为编号的球员
    # 获取i的下标
    
    # idx = score.index(i)
    
    # 去遍历更新
    for j in range(1, n + 1):
        score[j] = max(score[j], abs(j - i))
    # print(score)

print(*score[1:], sep = ' ')

# 1 0 1 2 3 4
# 2 1 0 1 2 3

# 60%
'''

n, m = map(int, input().split())
mi = float('inf')
ma = float('-inf')
x = list(map(int, input().split()))
for i in range(m):
    mi = min(x[i], mi)
    ma = max(x[i], ma)
for i in range(1, n + 1):
    print(max(abs(i - mi), abs(i - ma)), end=" " if i != n else "\n")

