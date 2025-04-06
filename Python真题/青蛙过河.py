import os
import sys
input = sys.stdin.readline
# 至少是多少满足条件的 -> 二分搜索判断
# y -> 不超过, 最多跳 y - 1格
# 每次要跳到石头或者直接跳过去
from itertools import accumulate


def check(y):
    # 每个长度为y的区间和大于等于2x就是可以跳的
    # 这里区间的和我们用前缀和记录
    # 长度为y的所有区间都支持被跳2 * x 下就是可以的
    for l in range(1, n - y + 1):
        r = l + y - 1
        if pre[r] - pre[l - 1] < 2 * x:
            # 有一个区间不符合
            return False
    return True
            


        


n, x = map(int, input().split())
# x = x << 1 # 过河次数
a = [0] + list(map(int, input().split()))
##pre = [0]*n
##for i in range(1, n):
##    pre[i] = pre[i-1] + a[i]
pre = list(accumulate(a))

# print(pre)

# 二分
l, r = 1, n
ans = l
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)


