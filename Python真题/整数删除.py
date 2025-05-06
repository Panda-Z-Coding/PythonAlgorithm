import os
import sys
import heapq
# 优先队列存储(值, 下标), 双向链表存储这个下标都前一个和后一个, 用两个next, pre 数组模拟
# 删除的话就修改指针

n, k = map(int, input().split())
a = [0] + list(map(int, input().split())) + [0] # 下标从1开始
# 我每次都重新建一个优先队列应该就可以了
l = [0] * (n + 2)
r = [0] * (n + 2)

l[n + 1] = n
r[0] = 1

# 最小堆
h = [] # 堆的懒更新
# ? 因为在堆中删除某个元素十分困难和费时间
# 所以当我们每次取出元素的时候我们和原来的数组进行比较
# 如果数组中的下标对应的值不是这个, 说明这个是旧的值
# 我们就要跳过当前选择

for i in range(1, n + 1):
    # 遍历数组, 建立双向链表
    l[i] = i - 1
    r[i] = i + 1
    heapq.heappush(h, (a[i], i))

# 这里要注意不能用for-continue
# ？因为Coninue会跳过这次但是k不会变
while k > 0:
    p = heapq.heappop(h)
    if p[0] != a[p[1]]: # 这里就是懒更新, 通过比较实时的值, 来确定是否是最新的值
        heapq.heappush(h, (a[p[1]], p[1]))
        k += 1
    else:
        # 删除
        idx = p[1]
        r[l[idx]] = r[idx]
        l[r[idx]] = l[idx]
        a[r[idx]] += a[idx]
        a[l[idx]] += a[idx]
    k -= 1

# 当前数组并没有被真实的修改
# 我们要按照指针来输出

head = r[0] # 定义一个指针
while head != n + 1:
    print(a[head], end = ' ')
    head = r[head]

    
    









