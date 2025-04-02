import sys
input = sys.stdin.readline
# from queue import PriorityQueue
# from collections import defaultdict
# import heapq
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
# 啊啊啊每次只能选相邻的两堆进行合并!!!
# 这样要用区间dp

# 因为是环, 可以将数组乘二
a = a * 2
nn = 2 * n
pres = list(accumulate(a, initial = 0))
# print(*pres)
# 1. 定义dp[i][j] 为区间[i, j] 的最大(最小)答案
dp1 = [[0] * (nn + 1) for i in range(nn + 1)] # 最大
dp2 = [[0] * (nn + 1) for i in range(nn + 1)] # 最小
inf = float('inf')
for le in range(2, n + 1): # 枚举区间长度
    for left in range(1, nn - le + 1 + 1):
        right = left + le - 1
        dp1[left][right] = -inf
        dp2[left][right] = inf

        for k in range(left, right):
            # 枚举中断点
            dp1[left][right] = max(dp1[left][right], dp1[left][k] + dp1[k + 1][right] + pres[right] - pres[left - 1])
            dp2[left][right] = min(dp2[left][right], dp2[left][k] + dp2[k + 1][right] + pres[right] - pres[left - 1])

min_s = inf
max_s = -inf
# 遍历所有长度为n的区间
for i in range(1, n + 1):
    min_s = min(min_s, dp2[i][i + n - 1])
    max_s = max(max_s, dp1[i][i + n - 1])

print(min_s)
print(max_s)



    
