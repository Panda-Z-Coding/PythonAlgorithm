import os
import sys


# 最长 的一根最短是多少 => 最长的哦!!!
'''
一直想错了，这个任意一更木棒切成两段，不是对半分，只不过要保证切成两段后都是整数
那么这种最大的最小值的问题 => 二分查找

1. 查找的值
    

check(x):
    把一个木棍剪成最大为x的若干个小段 => 次数 = [L // x] if L % x == 1 else [L // x] - 1
'''

n, m = map(int, input().split())
L = list(map(int, input().split()))

def check(x):
    # 检查是否能把每一个木棍都剪成最长的长度为x木棍并且花费<=m
    cnt = 0
    for a in L:
        # 遍历每一个木棍求出总的要砍到x至少花费
        if a > x:
            cnt += (a // x) # 草稿纸上面画就明白了
            if a % x == 0: # 偶数长度的时候少一次
                cnt -= 1
    return cnt <= m


## 二分查找
# [l, r]
l, r = 1, int(1e9)
ans = r
while l <= r:
    mid = (l + r) >> 1
    if check(mid):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1
print(ans)

# # [l, r)
# while l < r:
#     mid = (l + r) >> 1
#     if check(mid):
#         r = mid
#     else:
#         l = mid + 1

