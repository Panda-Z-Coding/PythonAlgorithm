# import os
# import sys
# n = int(input())
# a = list(map(int, input().split()))
# vis = {}
# for i in range(n):
#     while a[i] in vis:
#         a[i] += 1
#     vis[a[i]] = True
# print(*a)

def find(x):
    if fa[x] == x:
        return x
    else:
        fa[x] = find(fa[x]) # 路径压缩
        return fa[x]

def merge(x, y):
    fa[find(x)] = find(y)

n = int(input())
a = list(map(int,input().split()))

maxn = 1000010
fa = [i for i in range(maxn)]

for num in a:
    t = find(num)
    print(t, end = ' ')
    merge(t, t + 1)