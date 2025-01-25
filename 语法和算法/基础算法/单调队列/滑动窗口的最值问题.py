import os
import sys

# 请在此输入您的代码

from collections import deque
# 双端队列来实现滑动窗口的最值问题

n, m, a, b = list(map(int, input().split()))

A = [[] for i in range(n)] # 用来存矩阵
h = [[] for i in range(n)] # 用来存窗口是 (i, j) 的最大值
g = [[] for i in range(n)] # 用来存最小值

for i in range(n):
    A[i] = list(map(int, input().split()))
    q = deque() # 窗口, 可以放list, 相当于二维
    # 最小值
    for j in range(m): # 遍历每一行
        # 关键代码
        # 算法核心:
        '''
        deque 的左边只能出窗口之外的数据popleft
        deuqe 的右边只能进最小(最大)的数据, 其他的先pop掉
        '''
        #! 先弄(i,j)最小值
        while q and j - q[0][1] + 1 > b: q.popleft() # 左边的下标出现在了窗口外, 就popleft
        while q and q[-1][0] >= A[i][j]: q.pop() # 所有比[i][j]大的都pop出去
        q.append((A[i][j], j)) # 存储两个信息, 值和列标
        g[i].append(q[0][0]) # 把窗口的最大值存入g
    q.clear()
    # 最大值
    for j in range(m):
        while q and j - q[0][1] + 1 > b: q.popleft()
        while q and q[0][0] <= A[i][j]: q.pop()
        q.append((A[i][j], j))
        h[i].append(q[0][0])

for j in range(m): # 遍历列
    q = deque()
    for i in range(n):
        while q and i - q[0][1] + 1 > a: q.popleft()
        while q and q[-1][0] >= g[i][j]: q.pop()
        q.append((g[i][j], i))
        g[i][j] = q[0][0]
    q.clear()
    for i in range(n):
        while q and i - q[0][1] + 1 > a: q.popleft()
        while q and q[-1][0] <= h[i][j]: q.pop()
        q.append((h[i][j], i))
        h[i][j] = q[0][0]

ans = 0
for i in range(a - 1, n):
    for j in range(b - 1, m):
        ans += h[i][j] * g[i][j]
        ans %= 998244353
print(ans)
