import os
import sys

# 贪心的思路就是如果所有士兵分别训练一次花费总和比S贵的话就尽量全部人多练一点

n, s = map(int, input().split())
a = []
cur_all = 0 # 当前的全部单独训练一次的花费,如果当前全部单独训练花费小于S那就全部单独训练
for i in range(n):
    p, c = map(int, input().split())
    cur_all += p
    a.append([p, c]) # 0 -> 单独训练一次的花费， 1 -> 训练的次数

# 我觉得要先排序一下, 花费? 训练次数? 总花费?  => 还是按照训练次数升序吧
# 如果当前cur_all > 剩余的士兵分别训练的总和: 花费a[0][1] * S 最小的训练次数乘以全部训练的花费
# 取了第一个进行全体训练之后, 把第一个pop(0)
a.sort(key = lambda x : (x[1]))
# print(*a)
ans, temp = 0, 0
while cur_all > s:
    temp = a[0][1] # 记录最大能同时训练多少次
    ans = temp * s # 计算最大可能的集体训练花费
    # 消去
    cur_all -= a[0][0]
    a.pop(0)
for i in a:
    # 遍历剩余的士兵
    ans += i[0]*(i[1] - temp)
print(ans)
