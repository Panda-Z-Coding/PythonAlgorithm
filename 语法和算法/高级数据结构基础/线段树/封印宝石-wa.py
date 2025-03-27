import os
import sys

'''
通过线段树存储区间的最大值信息
之后通过单点更新删除已经取了的宝石
'''
class SegmentTree():
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.d = [0] * (4 * n)
        # self.pos = [0] * (4 * n) # 用于存储区间最大值来自那个下标
        # 自动建树
        self.build(0, self.n - 1, 1) # 下标都从0开始！！！
        # d的下标只能从1开始

    def build(self, s, t, p):
        if s == t:
            self.d[p] = self.arr[s]
            # self.pos[p] = s
            return 
        m = (s + t) >> 1
        self.build(s, m, p << 1)
        self.build(m + 1, t, p << 1 | 1)
        
        # merge
        self.d[p] = max(self.d[p << 1], self.d[p << 1 | 1])
        # self.pos[p] = self.arr.index(self.d[p]) # 查找最大值的下标
    # 查询
    def get_max(self, l, r, s, t, p):
        if l <= s and t <= r:
            return self.d[p]
        
        m = (s + t) >> 1
        cmax = 0
        if l <= m:
            cmax = max(cmax, self.get_max(l, r, s, m, p << 1))
        if r > m:
            cmax = max(cmax, self.get_max(l ,r, m + 1, t, p << 1 | 1))
        return cmax

    # 单点更新--删除节点--让节点的值为0
    def once_update(self, index, value, s, t, p):
        if s == t:
            self.d[p] = value
            return 
        
        m = (s + t) >> 1
        if index <= m:
            self.once_update(index, value, s, m, p << 1)
        else:
            self.once_update(index, value, m + 1, t, p << 1 | 1)

        # merge
        self.d[p] = max(self.d[p << 1], self.d[p << 1 | 1])
        # self.pos[p] = 

input = sys.stdin.readline
n, k = map(int, input().split())

arr = list(map(int, input().split()))

seg = SegmentTree(arr)

# print(*seg.arr)
# print(*seg.d)

ans = [-1] * (n)

# 从[i:]查找最大的并且还需要返回其下标, k -= j - i

for i in range(n):
    
    cur_max = seg.get_max(i, seg.n - 1, 0, seg.n - 1, 1)
    if cur_max == 0:
        break
    j = seg.arr.index(cur_max) # 获取当前元素的下标
    # 判断有没有力气封印
    if k > j - i:
        if cur_max != ans[max(i-1, 0)]:
            ans[i] = cur_max
            # 消耗体力
            k -= j - i
            # 删除cur_max
            seg.once_update(j, 0, 0, seg.n - 1, 1)
    else:
        # 拿当前对应位置放到盒子里不消耗体力
        # 如果当前对应的位置还有宝石的话, 就拿过来, 还要保证和前面不一样
        if seg.arr[i] != 0:
            ans[i] = seg.arr[i]
            # 删除seg.arr[i]
            seg.once_update(i, 0, 0, seg.n - 1, 1)
        else:
            break

print(*ans)









