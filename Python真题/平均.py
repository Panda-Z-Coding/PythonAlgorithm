import os
import sys
input = sys.stdin.readline

n = int(input())
tong = [0] * (10)
a = []
for i in range(n):
    ai, bi = map(int, input().split())
    tong[ai] += 1
    a.append((ai, bi))

a.sort(key = lambda x: (x[1], x))
# print(*a)
# 统计需要改变的次数
# 把0 -> n // 10
ci = n // 10
d = 0
for i in range(10):
    if tong[i] < ci:
        d += ci - tong[i]
# print(d)
# print(tong)
cost = 0
for i in range(n):
    if d == 0:
        break
    # 遍历a数组
    if tong[a[i][0]] > ci: # 有多
        cost += a[i][1]
        tong[a[i][0]] -= 1
        d -= 1
print(cost)
        


