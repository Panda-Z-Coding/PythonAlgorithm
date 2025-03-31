import os
import sys
import bisect
input = sys.stdin.readline
# 通俗理解题目的意思就是, (xi, yi) 在 (xj, yj) 的左下方

# 这种就是有两个条件需要满足的, 就很像树状数组 -> 先满足一个之后另一个用树状数组来记录

class TreeArray():
    def __init__(self, n):
        self.data = [0] * (n + 1)
        self.n = n + 1 # 树状数组的下标从1开始

    def lowbit(self, x):
        return x & (-x)
    
    def add(self, index, x):
        while index < self.n:
            self.data[index] += x
            index += self.lowbit(index)
    
    def query(self, index):
        ans = 0
        while index > 0:
            ans += self.data[index]
            index -= self.lowbit(index)
        return ans

n = int(input())
a = [tuple(map(int, input().split())) for i in range(n)]

# 先对x做排序 满足 xi <= xj
a.sort()

# 现在对y进行离散化处理, 减少数据的复杂度
y = [j for _, j in a]
y = sorted(set(y))

ta = TreeArray(len(y))
ans = 0

for i, j in a:
    idx = bisect.bisect_right(y, j)
    ans += ta.query(idx)
    ta.add(idx, 1)

print(ans)