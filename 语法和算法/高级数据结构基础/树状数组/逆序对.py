import os
import sys

# 通过树状数组的下标来表示前面处理过的参数个数

def lowbit(x):
    return x & (-x)

def add(index, tree):
    # 在index加上a
    while index <= len(tree):
        tree[index] += 1 # 没处理过了, 加一
        index += lowbit(index)
    
def query(index, tree):
    ans = 0
    while index:
        ans += tree[index]
        index -= lowbit(index)
    return ans


# 输入输出？？
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
N = int(1e6 + 7)
ta = [0] * (N + 1) # 树状数组

# 遍历到当前位置的话肯定满足 j > i 这个条件
# 我们通过树状数组的下标表示被处理过的参数大小, 在这之前的都是比自己小的 => 也就是不符合条件的
# 我们可以先假设前面的所有都满足条件, 之后再减去不符合的情况
ans = 0
for i in range(1, n + 1):
    ans += (i - 1) - query(a[i], ta) # 先假设当前位置之前的所有都满足，之后减去比自己小的个数（不符合的数量）
    add(a[i], ta) # 更新

print(ans)