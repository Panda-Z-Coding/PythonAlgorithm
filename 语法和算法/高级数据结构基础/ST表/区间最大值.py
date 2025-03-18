# ST表
'''
- 适用的问题 => RMQ 求区间的最大/最小值的问题

- 可重复贡献问题: 对于运算opt 满足 x opt x = x, 且满足运算结合律
对应的区间就是可重复贡献问题
'''

import os
import sys
import math
n, q = map(int, input().split())
a = list(map(int, input().split()))
'''==最大值ST=='''
def st_init(n, a):
    L = math.ceil(math.log2(n)) + 1 # 最长的2次幂长度
    f = [[0] * L for i in range(n)]
    # 边界
    for i in range(n):
        f[i][0] = a[i]
    # 先枚举j再枚举i
    for j in range(1, L):
        pj = 1 << (j - 1)
        for i in range(n - pj): # 注意 n - pj
            f[i][j] = max(f[i][j - 1], f[i + pj][j - 1])
    return f

def query(f, l, r):
    s = int(math.log2(r - l + 1))
    return max(f[l][s], f[r - (1 << s) + 1][s])

# ==最小值ST==
def st_min_init(n, a):
    L = math.ceil(math.log2(n)) + 1
    f = [[0] * L for i in range(n)]
    # 处理边界
    for i in range(n):
        f[i][0] = a[i]
    # 先j后i
    for j in range(1, L):
        pj = 1 << (j - 1)
        for i in range(n - pj):
            f[i][j] = min(f[i][j-1], f[i + pj][j - 1])
    return f
def query_min(f, l, r):
    s = int(math.log2(r - l + 1))
    return min(f[l][s], f[r - (1 << s) + 1][s])

f = st_min_init(n ,a)
for i in range(q):
    l, r = map(int, input().split())
    # 注意下标从0开始
    l, r = l - 1, r - 1
    print(query_min(f, l, r))
