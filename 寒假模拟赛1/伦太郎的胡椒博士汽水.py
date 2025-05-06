# 用单调队列来维护区间的最大最小值问题
import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 用两个单调队列来维护最值
qmin = deque() # 存储元素的下标位置
qmax = deque()

# 不断枚举左右区间
i, j = 0, 0
ans = 0
while i < n:
    while j < n:
        while qmax and a[qmax[-1]] <= a[j]:
            qmax.pop()
        qmax.append(j)
        # 维护最小就把这里面比要进来的小的pop
        while qmin and a[qmin[-1]] >= a[j]:
            qmin.pop()
        qmin.append(j)
        # 剪枝
        if a[qmax[0]] - a[qmin[0]] > k:
            break
        j += 1
    # 判断队首元素还在不在区间内
    if qmax[0] == i:
        qmax.popleft()
    if qmin[0] == i: # == i 是因为我马上就要往下一个i走了
        # 如果当前区间最大的是左边区间
        # 那它下一步就是要超出区间了
        qmin.popleft()

    # 计算答案
    # 因为我只要是j能往前走, 我都是符合条件的区间
    ans += j - i - 1
    i += 1

print(ans)

        
