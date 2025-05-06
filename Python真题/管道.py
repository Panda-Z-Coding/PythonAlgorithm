import os
import sys
input = sys.stdin.readline

n, le = map(int, input().split())
# 存储每个阀门的打开时刻
time = {} # 用字典存储
for i in range(n):
    L, S = map(int, input().split())
    time[L] = S
# print(time)
def check(mid):
    # 用合并区间的做法来看最后合并下来的区间是否是整个区间
    # 枚举左边的区间, 更新当前最右边的区间
    # 先求出所有的区间, 然后进行排序
    q = []
    for i, temp in time.items():
        # 在管道的位置, 开闸的时刻
        if temp <= mid:
            # 如果当前位置开闸时刻小于mid
            # 计算覆盖区间
            q.append([i - (mid - temp), i + (mid - temp)])
    q.sort() # 按照左边界来排序
    if q[0][0] > 1:
        return False  
    cur_r = q[0][1] # 记录和更新当前最右边的边界
    # 进行合并
    for i in range(1, len(q)):
        if q[i][0] - cur_r <= 1:
            # 当前的右边边界小于最大的左边边界, 合并为一个区间
            cur_r = max(cur_r, q[i][1])
        else:
            # 这两个区间断开了直接返回
            return False
    return cur_r >= le # 最右边能不能大于长度
        

    
# print(check(5))


# 二分查找
l, r = 1, 10**9
ans = l
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)

